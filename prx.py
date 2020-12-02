from dongle import Dongle

PRX_SLAVE_ADDR = 0x24

class Prx():
    def __init__(self):
        self.dgl = Dongle()
        pass

    def connect(self):
        self.dgl.open(b'FT4222 A')
        self.isc_enter()
        self.getid()
        self.isc_exit()

    def disconnect(self):
        self.dgl.close()

    def isc_enter(self):
        cmd = [0xFB, 0x4A, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)

    def isc_exit(self):
        cmd = [0xFB, 0x4A, 0x00, 0x66, 0x00, 0x00, 0x00, 0x00]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)

    def getid(self):
        cmd = [0xFB, 0x4A, 0x50, 0xC2, 0x00, 0x00, 0x00, 0x00]
        self.dgl.write(PRX_SLAVE_ADDR, cmd)
        data = self.dgl.read(PRX_SLAVE_ADDR, 2)
        id = (data[0] << 8) | data[1]
        print("CHIP ID: " + hex(id))
        return id
