import os
import time
import logging
from  cfs.dongle import Dongle

PRX_SLAVE_ADDR = 0x24

class Prx():
    def __init__(self):
        self.dgl = Dongle()
        self.connected = 0

    def _readbin(self, binfile):
        size = os.path.getsize(binfile)
        with open(binfile, 'rb') as f:
            content = f.read(size)
            return list(bytes(content))

    def connect(self, desc):
        self.enb(0)
        if self.dgl.open(desc) == False:
            return False
        self.connected = 1
        self.isc_enter()
        self.getid()
        self.isc_exit()
        return True

    def disconnect(self):
        if self.connected == 1:
            self.dgl.close()
        self.enb(1)
        self.connected = 0
    
    def reconnect(self):
        time.sleep(0.1)
        self.disconnect()
        time.sleep(0.1)
        self.connect(b'FT4222 A')

    def isc_enter(self):
        cmd = [ 0xFB, 
                0x4A, 
                0x00, 
                0x65, 
                0x00, 
                0x00, 
                0x00, 
                0x00 ]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)

    def isc_exit(self):
        cmd = [ 0xFB, 
                0x4A, 
                0x00, 
                0x66, 
                0x00, 
                0x00, 
                0x00, 
                0x00 ]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)

    def getid(self):
        cmd = [ 0xFB, 
                0x4A, 
                0x50, 
                0xC2, 
                0x00, 
                0x00, 
                0x00, 
                0x00 ]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)
        data = self.dgl.read(PRX_SLAVE_ADDR, 2)
        id = (data[0] << 8) | data[1]
        print("CHIP ID: " + hex(id))
        return id

    def writesram(self, addr, data):
        cmd = [ 0xFB, 
                0x4A, 
                0xE0, 
                0xA0, 
                (addr >> 24) & 0xFF,
                (addr >> 16) & 0xFF,
                (addr >> 8)  & 0xFF,
                (addr >> 0)  & 0xFF,
                data ]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)

    def wait(self, timeout):
        cmd = [ 0xFB, 
                0x4A, 
                0x36, 
                0xC2, 
                0x00, 
                0x00, 
                0x00, 
                0x00 ]
        t = 0
        while (t < timeout):
            t += 0.25
            time.sleep(0.25)
            self.dgl.write(PRX_SLAVE_ADDR, cmd)
            buf = self.dgl.read(PRX_SLAVE_ADDR, 1)
            if buf[0] == 0xAD:
                return True
        return False

    def enb(self, state):
        self.dgl.port2_write(state)

    def regset(self, addr, data):
        cmd = []
        if (addr & 0xFFFF0000) == 0x50100000:
            cmd.append(addr & 0xff)
            cmd.append(0x51)
            cmd.append(data)
        elif (addr & 0xFFFF0000) == 0x500E0000:
            cmd.append(addr & 0xff)
            cmd.append(0x5E)
            cmd.append(data)
        elif (addr & 0xFFFF0000) == 0x38000000:
            cmd.append(addr & 0xff)
            cmd.append(0x38)
            cmd.append(data)
        elif (addr & 0xFFFF0000) == 0x00000000:
            cmd.append(addr & 0xff)
            cmd.append(0x00)
            cmd.append(data)
        elif (addr & 0xFFFF0000) == 0x50020000:
            cmd.append(addr & 0xff)
            cmd.append(0x52)
            cmd.append(data)
        else:
            return
        self.dgl.write(PRX_SLAVE_ADDR, cmd)
        
    def regget(self, addr):
        cmd = []
        if (addr & 0xFFFF0000) == 0x50100000:
            cmd.append(addr & 0xff)
            cmd.append(0x51)
        elif (addr & 0xFFFF0000) == 0x500E0000:
            cmd.append(addr & 0xff)
            cmd.append(0x5E)
        elif (addr & 0xFFFF0000) == 0x38000000:
            cmd.append(addr & 0xff)
            cmd.append(0x38)
        elif (addr & 0xFFFF0000) == 0x00000000:
            cmd.append(addr & 0xff)
            cmd.append(0x00)
        elif (addr & 0xFFFF0000) == 0x50020000:
            cmd.append(addr & 0xff)
            cmd.append(0x52)
        else:
            return
        self.dgl.write(PRX_SLAVE_ADDR, cmd)
        data = self.dgl.read(PRX_SLAVE_ADDR, 1)
        return data[0]

    def readpage(self, addr, size):
        cmd = [ 0xFB, 
                0x4A, 
                0x00, 
                0xC2, 
                (addr >> 24) & 0xFF,
                (addr >> 16) & 0xFF,
                (addr >> 8)  & 0xFF,
                (addr >> 0)  & 0xFF ]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)
        return self.dgl.read(PRX_SLAVE_ADDR, size)

    def writepage(self, addr, data, size):
        cmd = [ 0xFB, 
                0x4A, 
                0x00, 
                0xA5,
                (addr >> 24) & 0xFF,
                (addr >> 16) & 0xFF,
                (addr >> 8)  & 0xFF,
                (addr >> 0)  & 0xFF ]
        self.dgl.write(PRX_SLAVE_ADDR, cmd + data)
        return self.wait(3)
    
    def download(self, binfile='', verify=0):
        content = self._readbin(binfile)
        if len(content) == 0:
            return False
        address = 0
        pagesize = 1024
        totalsize = len(content)
        while totalsize > 0:
            if totalsize > pagesize:
                self.writepage(address, content[address:(address + pagesize)], pagesize)
                if verify:
                    verifydata = self.readpage(address, pagesize)
                    if verifydata != content[address:(address + pagesize)]:
                        return False
                totalsize -= pagesize
                address += pagesize
                print('#', end='')
            else:
                self.writepage(address, content[address:], totalsize)
                if verify:
                    verifydata = self.readpage(address, totalsize)
                    if verifydata != content[address:]:
                        return False
                totalsize = 0
                print('#')
        return True

    def get_logline(self):
        try:
            data = self.dgl.read(PRX_SLAVE_ADDR, 256)
            logline = bytes([d for d in data if d != 0x0a and d != 0xe7]).decode('utf-8', 'strict')
            if len(logline) > 0:
                return logline
        except UnicodeDecodeError:
            pass

    def get_log(self):
        while True:
            try:
                data = self.dgl.read(PRX_SLAVE_ADDR, 256)
                logline = bytes([d for d in data if d != 0x0a and d != 0xe7]).decode('utf-8', 'strict')
                if len(logline) > 0:
                    logging.info(logline)
            except UnicodeDecodeError:
                pass