# -*- coding: utf-8 -*-
from . import _ft4222 as _ft
import ctypes as c
from .defines import *
import threading

msgs = {
    0: 'OK',
    1: 'INVALID_HANDLE',
    2: 'DEVICE_NOT_FOUND',
    3: 'DEVICE_NOT_OPENED',
    4: 'IO_ERROR',
    5: 'INSUFFICIENT_RESOURCES',
    6: 'INVALID_PARAMETER',
    7: 'INVALID_BAUD_RATE',
    8: 'DEVICE_NOT_OPENED_FOR_ERASE',
    9: 'DEVICE_NOT_OPENED_FOR_WRITE',
    10: 'FAILED_TO_WRITE_DEVICE',
    11: 'EEPROM_READ_FAILED',
    12: 'EEPROM_WRITE_FAILED',
    13: 'EEPROM_ERASE_FAILED',
    14: 'EEPROM_NOT_PRESENT',
    15: 'EEPROM_NOT_PROGRAMMED',
    16: 'INVALID_ARGS',
    17: 'NOT_SUPPORTED',
    18: 'OTHER_ERROR',
    19: 'DEVICE_LIST_NOT_READY',
    1000: 'DEVICE_NOT_SUPPORTED',
    1001: 'CLK_NOT_SUPPORTED',
    1002: 'VENDER_CMD_NOT_SUPPORTED',
    1003: 'IS_NOT_SPI_MODE',
    1004: 'IS_NOT_I2C_MODE',
    1005: 'IS_NOT_SPI_SINGLE_MODE',
    1006: 'IS_NOT_SPI_MULTI_MODE',
    1007: 'WRONG_I2C_ADDR',
    1008: 'INVAILD_FUNCTION',
    1009: 'INVALID_POINTER',
    1010: 'EXCEEDED_MAX_TRANSFER_SIZE',
    1011: 'FAILED_TO_READ_DEVICE',
    1012: 'I2C_NOT_SUPPORTED_IN_THIS_MODE',
    1013: 'GPIO_NOT_SUPPORTED_IN_THIS_MODE',
    1014: 'GPIO_EXCEEDED_MAX_PORTNUM',
    1015: 'GPIO_WRITE_NOT_SUPPORTED',
    1016: 'GPIO_PULLUP_INVALID_IN_INPUTMODE',
    1017: 'GPIO_PULLDOWN_INVALID_IN_INPUTMODE',
    1018: 'GPIO_OPENDRAIN_INVALID_IN_OUTPUTMODE',
    1019: 'INTERRUPT_NOT_SUPPORTED',
    1020: 'GPIO_INPUT_NOT_SUPPORTED',
    1021: 'EVENT_NOT_SUPPORTED'
}

lock=threading.Lock()

class DeviceError(Exception):
    """Exception class for status messages"""
    def __init__(self, msgnum):
        self.message = msgs[msgnum]

    def __str__(self):
        return self.message

def call_ft(function, *args):
    """Call an FTDI function and check the status. Raise exception on error"""
    lock.acquire()
    status = function(*args)
    if status != _ft.FT4222_OK:
        print(DeviceError(status))
    lock.release()

def SetClock(h, clk):
    call_ft(_ft.FT4222_SetClock, h, _ft.DWORD(clk))

def SetSuspendOut(h, enable):
    call_ft(_ft.FT4222_SetSuspendOut, h, _ft.BOOL(enable))

def SetWakeUpInterrupt(h, enable):
    call_ft(_ft.FT4222_SetWakeUpInterrupt, h, _ft.BOOL(enable))
    
def SetInterruptTrigger(h,portNum):
    call_ft(_ft.FT4222_SetInterruptTrigger,h,_ft.DWORD(portNum))

def GPIO_Init(h, dir0, dir1, dir2, dir3):
    d = (c.c_uint32 * 4)()
    d[0] = dir0
    d[1] = dir1
    d[2] = dir2
    d[3] = dir3
    call_ft(_ft.FT4222_GPIO_Init, h, d)

def I2CMaster_Reset(h):
    call_ft(_ft.FT4222_I2CMaster_Reset, h)

def UnInitialize(h):
    call_ft(_ft.FT4222_UnInitialize, h)

def GPIO_Write(h, portNum, bValue):
    call_ft(_ft.FT4222_GPIO_Write, h, _ft.DWORD(portNum), _ft.BOOL(bValue))

def GPIO_Read(h, portNum):
    bValue = _ft.BOOL()
    call_ft(_ft.FT4222_GPIO_Read, h, _ft.DWORD(portNum), c.byref(bValue))
    return bValue.value

def I2CMaster_Init(h, kbps):
    call_ft(_ft.FT4222_I2CMaster_Init, h, _ft.DWORD(kbps))

def I2CMaster_Write(h, addr, buf, size):
    b = (c.c_ubyte * size)()
    for i, d in enumerate(buf):
        b[i] = d
    transferred = _ft.WORD()
    call_ft(_ft.FT4222_I2CMaster_Write, h, _ft.WORD(addr), b, _ft.WORD(size),
            c.byref(transferred))
    return transferred.value

def I2CMaster_Read(h, addr, size):
    d = (c.c_ubyte * size)()
    transferred = _ft.WORD()
    call_ft(_ft.FT4222_I2CMaster_Read, h, _ft.WORD(addr), d, _ft.WORD(size),
            c.byref(transferred))
    return list(d)

def GPIO_GetTriggerStatus(h, portNum):
    Value=_ft.WORD()
    call_ft(_ft.FT4222_GPIO_GetTriggerStatus,h,_ft.DWORD(portNum),c.byref(Value))
    return Value.value