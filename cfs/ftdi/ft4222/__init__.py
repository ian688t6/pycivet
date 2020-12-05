"""
Control FTDI USB chips.

There are a few convinience functions too
"""
import sys

from .ft4222 import *

__all__ = [
    'call_ft', 'SetClock', 'SetSuspendOut', 'SetWakeUpInterrupt', 'GPIO_Init',
    'I2CMaster_Reset', 'UnInitialize', 'GPIO_Write', 'I2CMaster_Init',
    'I2CMaster_Write', 'I2CMaster_Read'
]

if sys.platform == 'win32':
    __all__ += ['w32CreateFile']
else:
    __all__ += ['getVIDPID', 'setVIDPID']
