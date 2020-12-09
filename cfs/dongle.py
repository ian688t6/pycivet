from cfs.ftdi.ftd2xx._ftd2xx import *
from cfs.ftdi.ftd2xx.defines import *
import cfs.ftdi.ftd2xx as ftd2xx
import cfs.ftdi.ft4222 as ft4222
import cfs.ftdi.mpsse  as mpsse

class Dongle():
    def __init__(self):
        self.devs = []
        numOfDevices = ftd2xx.createDeviceInfoList()
        for iDev in range(numOfDevices):
            devinfo = ftd2xx.getDeviceInfoDetail(iDev)
            self.devs.append(devinfo)     

    def open(self, devname):
        if len(self.devs) == 0:
            return False
        for d in self.devs:
            if d['description'] == devname:
                print('open ' + str(devname))
                self._desc = devname
                if d['description'] == b'FT4222 A' or d['description'] == b'FT4222 B':
                    self.ft = ftd2xx.openEx(d['location'], OPEN_BY_LOCATION)
                    ft4222.SetClock(self.ft.handle, 400)
                    ft4222.I2CMaster_Init(self.ft.handle, 400)
                elif d['description'] == b'UM232H':
                    self.ft232 = mpsse.I2CMaster()
                    self.ft232.Init_libMPSSE() # Graceful initialization
                    self.ft232.GetNumChannels()
                    self.ft232.GetChannelInfo() # Channel index starts at 0
                    self.ft232.OpenChannel() # Assign handle to channel 0
                    self.ft232.InitChannel('Fast') # Configure I2C port in 100kHz mode
                return True
        return False

    def close(self):
        if self._desc == b'FT4222 A' or self._desc == b'FT4222 B':
            ft4222.I2CMaster_Reset(self.ft.handle)
            ft4222.UnInitialize(self.ft.handle)
            self.ft.close()
        elif self._desc == b'UM232H':
            self.ft232.CloseChannel()
            self.ft232.Cleanup_libMPSSE()
    
    def read(self, slave, len):
        if self._desc == b'FT4222 A' or self._desc == b'FT4222 B':
            return ft4222.I2CMaster_Read(self.ft.handle, slave, len)
        elif self._desc == b'UM232H':
            return self.ft232.I2CMaster_Read(slave, len)

    def write(self, slave, data):
        if self._desc == b'FT4222 A' or self._desc == b'FT4222 B':
            ft4222.I2CMaster_Write(self.ft.handle, slave, data, len(data))
        elif self._desc == b'UM232H':
            return self.ft232.I2CMaster_Write(slave, data, len(data))
