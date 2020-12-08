import os
import time
import logging
from  cfs.dongle import Dongle

PRX_SLAVE_ADDR = 0x24

class Prx():
    def __init__(self):
        self.dgl = Dongle()
        pass

    def _readbin(self, binfile):
        size = os.path.getsize(binfile)
        with open(binfile, 'rb') as f:
            content = f.read(size)
            return list(bytes(content))

    def connect(self, desc):
        self.dgl.open(desc)
        self.isc_enter()
        self.getid()
        self.isc_exit()

    def disconnect(self):
        self.dgl.close()

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

    def getlog(self):
        while True:
            try:
                data = self.dgl.read(PRX_SLAVE_ADDR, 256)
                logline = bytes([d for d in data if d != 0x0a and d != 0xe7]).decode('utf-8', 'strict')
                if len(logline) > 0:
                    logging.info(logline)
            except UnicodeDecodeError:
                pass