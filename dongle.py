from ftdi.ftd2xx._ftd2xx import *
from ftdi.ftd2xx.defines import *
import logging
import ftdi.ftd2xx as ftd2xx
import ftdi.ft4222 as ft4222

class Dongle():
    def __init__(self):
        self.devs = []
        numOfDevices = ftd2xx.createDeviceInfoList()
        for iDev in range(numOfDevices):
            devinfo = ftd2xx.getDeviceInfoDetail(iDev)
            self.devs.append(devinfo)     

    def open(self, devname):
        for d in self.devs:
            if d['description'] == devname:
                print('open ' + str(devname))
                self.ft = ftd2xx.openEx(d['location'], OPEN_BY_LOCATION)
                ft4222.SetClock(self.ft.handle, 400)
                ft4222.I2CMaster_Init(self.ft.handle, 400)
                break

    def close(self):
        ft4222.I2CMaster_Reset(self.ft.handle)
        ft4222.UnInitialize(self.ft.handle)
        self.ft.close()
        pass
    
    def read(self, slave, len):
        return ft4222.I2CMaster_Read(self.ft.handle, slave, len)

    def write(self, slave, data):
        ft4222.I2CMaster_Write(self.ft.handle, slave, data, len(data))
