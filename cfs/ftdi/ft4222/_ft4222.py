# -*- coding: utf-8 -*-
import platform
from ctypes import *

DWORD   = c_uint32
ULONG   = c_uint32
WORD    = c_uint16
BYTE    = c_uint8
BOOL    = c_int
BOOLEAN = c_char
LPCSTR  = c_char_p
HANDLE  = c_void_p
LONG    = c_long
UINT    = c_uint
LPSTR   = c_char_p

if platform.architecture()[0] == '64bit':
    ft4222 = CDLL('./LibFT4222-64.dll')
else:
    ft4222 = CDLL('./LibFT4222.dll')

# LibFT4222.h 67
FT4222_EVENT_RXCHAR                          = 8

# LibFT4222.h 68
# spi slave sync word
FT4222_SPI_SLAVE_SYNC_WORD                   = 0x5A

# LibFT4222.h 71
# spi slave cmd
SPI_MASTER_TRANSFER                          = 0x80
SPI_SLAVE_TRANSFER                           = 0x81
SPI_SHORT_MASTER_TRANSFER                    = 0x82
SPI_SHART_SLAVE_TRANSFER                     = 0x83
SPI_ACK                                      = 0x84

# LibFT4222.h 83
# FT4222 Device status
FT4222_OK                                    = 0
FT4222_INVALID_HANDLE                        = 1
FT4222_DEVICE_NOT_FOUND                      = 2
FT4222_DEVICE_NOT_OPENED                     = 3
FT4222_IO_ERROR                              = 4
FT4222_INSUFFICIENT_RESOURCES                = 5
FT4222_INVALID_PARAMETER                     = 6
FT4222_INVALID_BAUD_RATE                     = 7
FT4222_DEVICE_NOT_OPENED_FOR_ERASE           = 8
FT4222_DEVICE_NOT_OPENED_FOR_WRITE           = 9
FT4222_FAILED_TO_WRITE_DEVICE                = 10
FT4222_EEPROM_READ_FAILED                    = 11
FT4222_EEPROM_WRITE_FAILED                   = 12
FT4222_EEPROM_ERASE_FAILED                   = 13
FT4222_EEPROM_NOT_PRESENT                    = 14
FT4222_EEPROM_NOT_PROGRAMMED                 = 15
FT4222_INVALID_ARGS                          = 16
FT4222_NOT_SUPPORTED                         = 17
FT4222_OTHER_ERROR                           = 18
FT4222_DEVICE_LIST_NOT_READY                 = 19

FT4222_DEVICE_NOT_SUPPORTED                  = 1000  # FT_STATUS extending message
FT4222_CLK_NOT_SUPPORTED                     = 1001  # spi master do not support 80MHz/CLK_2
FT4222_VENDER_CMD_NOT_SUPPORTED              = 1002
FT4222_IS_NOT_SPI_MODE                       = 1003
FT4222_IS_NOT_I2C_MODE                       = 1004
FT4222_IS_NOT_SPI_SINGLE_MODE                = 1005
FT4222_IS_NOT_SPI_MULTI_MODE                 = 1006
FT4222_WRONG_I2C_ADDR                        = 1007
FT4222_INVAILD_FUNCTION                      = 1008
FT4222_INVALID_POINTER                       = 1009
FT4222_EXCEEDED_MAX_TRANSFER_SIZE            = 1010
FT4222_FAILED_TO_READ_DEVICE                 = 1011
FT4222_I2C_NOT_SUPPORTED_IN_THIS_MODE        = 1012
FT4222_GPIO_NOT_SUPPORTED_IN_THIS_MODE       = 1013
FT4222_GPIO_EXCEEDED_MAX_PORTNUM             = 1014
FT4222_GPIO_WRITE_NOT_SUPPORTED              = 1015
FT4222_GPIO_PULLUP_INVALID_IN_INPUTMODE      = 1016
FT4222_GPIO_PULLDOWN_INVALID_IN_INPUTMODE    = 1017
FT4222_GPIO_OPENDRAIN_INVALID_IN_OUTPUTMODE  = 1018
FT4222_INTERRUPT_NOT_SUPPORTED               = 1019
FT4222_GPIO_INPUT_NOT_SUPPORTED              = 1020
FT4222_EVENT_NOT_SUPPORTED                   = 1021

PVOID = c_void_p

# LibFT4222.h 224
class FT4222_Version(Structure):
    _pack_ = 1
    _fields_ = [("chipVersion", DWORD),
                ("dllVersion",  DWORD)]

# LibFT4222.h 232
class SPI_Slave_Header(Structure):
    _pack_ = 1
    _fields_ = [("syncWord", BYTE),
                ("cmd",      BYTE),
                ("sn",       BYTE),
                ("size",     BYTE)]

FT_HANDLE = PVOID
FT_STATUS = ULONG

# FT4222 General Functions
# LibFT4222.h 249
FT4222_UnInitialize = ft4222.FT4222_UnInitialize
FT4222_UnInitialize.restype = FT_STATUS
# FT4222_STATUS FT4222_UnInitialize(FT_HANDLE ftHandle);
FT4222_UnInitialize.argtypes = [FT_HANDLE]
FT4222_UnInitialize.__doc__ = \
    """FT4222_STATUS FT4222_UnInitialize(FT_HANDLE ftHandle);
ftd2xx.h:249"""

# LibFT4222.h 250
FT4222_SetClock = ft4222.FT4222_SetClock
FT4222_SetClock.restype = FT_STATUS
# FT4222_STATUS FT4222_SetClock(FT_HANDLE ftHandle, FT4222_ClockRate clk);
FT4222_SetClock.argtypes = [FT_HANDLE, DWORD]
FT4222_SetClock.__doc__ = \
    """FT4222_STATUS FT4222_SetClock(FT_HANDLE ftHandle, FT4222_ClockRate clk);
ftd2xx.h:250"""

# LibFT4222.h 251
FT4222_GetClock = ft4222.FT4222_GetClock
FT4222_GetClock.restype = FT_STATUS
# FT4222_STATUS FT4222_GetClock(FT_HANDLE ftHandle, FT4222_ClockRate* clk);
FT4222_GetClock.argtypes = [FT_HANDLE, POINTER(DWORD)]
FT4222_GetClock.__doc__ = \
    """FT4222_STATUS FT4222_GetClock(FT_HANDLE ftHandle, FT4222_ClockRate* clk);
ftd2xx.h:251"""

# LibFT4222.h 252
FT4222_SetWakeUpInterrupt = ft4222.FT4222_SetWakeUpInterrupt
FT4222_SetWakeUpInterrupt.restype = FT_STATUS
# FT4222_STATUS FT4222_SetWakeUpInterrupt(FT_HANDLE ftHandle, BOOL enable);
FT4222_SetWakeUpInterrupt.argtypes = [FT_HANDLE, BOOL]
FT4222_SetWakeUpInterrupt.__doc__ = \
    """FT4222_STATUS FT4222_SetWakeUpInterrupt(FT_HANDLE ftHandle, BOOL enable);
ftd2xx.h:252"""

# LibFT4222.h 253
FT4222_SetInterruptTrigger = ft4222.FT4222_SetInterruptTrigger
FT4222_SetInterruptTrigger.restype = FT_STATUS
# FT4222_STATUS FT4222_SetInterruptTrigger(FT_HANDLE ftHandle, GPIO_Tigger trigger);
FT4222_SetInterruptTrigger.argtypes = [FT_HANDLE, DWORD]
FT4222_SetInterruptTrigger.__doc__ = \
    """FT4222_STATUS FT4222_SetInterruptTrigger(FT_HANDLE ftHandle, GPIO_Tigger trigger);
ftd2xx.h:253"""

# LibFT4222.h 254
FT4222_SetSuspendOut = ft4222.FT4222_SetSuspendOut
FT4222_SetSuspendOut.restype = FT_STATUS
# FT4222_STATUS FT4222_SetSuspendOut(FT_HANDLE ftHandle, BOOL enable);
FT4222_SetSuspendOut.argtypes = [FT_HANDLE, BOOL]
FT4222_SetSuspendOut.__doc__ = \
    """FT4222_STATUS FT4222_SetSuspendOut(FT_HANDLE ftHandle, BOOL enable);
ftd2xx.h:254"""

# LibFT4222.h 255
FT4222_GetMaxTransferSize = ft4222.FT4222_GetMaxTransferSize
FT4222_GetMaxTransferSize.restype = FT_STATUS
# FT4222_STATUS FT4222_GetMaxTransferSize(FT_HANDLE ftHandle, uint16* pMaxSize);
FT4222_GetMaxTransferSize.argtypes = [FT_HANDLE, POINTER(WORD)]
FT4222_GetMaxTransferSize.__doc__ = \
    """FT4222_STATUS FT4222_GetMaxTransferSize(FT_HANDLE ftHandle, uint16* pMaxSize);
ftd2xx.h:255"""

# LibFT4222.h 256
FT4222_SetEventNotification = ft4222.FT4222_SetEventNotification
FT4222_SetEventNotification.restype = FT_STATUS
# FT4222_STATUS FT4222_SetEventNotification(FT_HANDLE ftHandle, DWORD mask, PVOID param);
FT4222_SetEventNotification.argtypes = [FT_HANDLE, DWORD, PVOID]
FT4222_SetEventNotification.__doc__ = \
    """FT4222_STATUS FT4222_SetEventNotification(FT_HANDLE ftHandle, DWORD mask, PVOID param);
ftd2xx.h:256"""

# LibFT4222.h 257
FT4222_GetVersion = ft4222.FT4222_GetVersion
FT4222_GetVersion.restype = FT_STATUS
# FT4222_STATUS FT4222_GetVersion(FT_HANDLE ftHandle, FT4222_Version* pVersion);
FT4222_GetVersion.argtypes = [FT_HANDLE, POINTER(DWORD)]
FT4222_GetVersion.__doc__ = \
    """FT4222_STATUS FT4222_GetVersion(FT_HANDLE ftHandle, FT4222_Version* pVersion);
ftd2xx.h:257"""

# FT4222 SPI Functions
# LibFT4222.h 262
FT4222_SPIMaster_Init = ft4222.FT4222_SPIMaster_Init
FT4222_SPIMaster_Init.restype = FT_STATUS
# FT4222_STATUS FT4222_SPIMaster_Init(FT_HANDLE ftHandle, FT4222_SPIMode  ioLine, FT4222_SPIClock clock, FT4222_SPICPOL  cpol, FT4222_SPICPHA  cpha, uint8 ssoMap);
FT4222_SPIMaster_Init.argtypes = [FT_HANDLE, DWORD, DWORD, DWORD, DWORD, BYTE]
FT4222_SPIMaster_Init.__doc__ = \
    """FT4222_STATUS FT4222_SPIMaster_Init(FT_HANDLE ftHandle, FT4222_SPIMode  ioLine, FT4222_SPIClock clock, FT4222_SPICPOL  cpol, FT4222_SPICPHA  cpha, uint8 ssoMap);
ftd2xx.h:262"""

# LibFT4222.h 263
FT4222_SPIMaster_SetLines = ft4222.FT4222_SPIMaster_SetLines
FT4222_SPIMaster_SetLines.restype = FT_STATUS
# FT4222_STATUS FT4222_SPIMaster_SetLines(FT_HANDLE ftHandle, FT4222_SPIMode spiMode);
FT4222_SPIMaster_SetLines.argtypes = [FT_HANDLE, DWORD]
FT4222_SPIMaster_SetLines.__doc__ = \
    """FT4222_STATUS FT4222_SPIMaster_SetLines(FT_HANDLE ftHandle, FT4222_SPIMode spiMode);
ftd2xx.h:263"""

# LibFT4222.h 264
FT4222_SPIMaster_SingleRead = ft4222.FT4222_SPIMaster_SingleRead
FT4222_SPIMaster_SingleRead.restype = FT_STATUS
# FT4222_STATUS FT4222_SPIMaster_SingleRead(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeOfRead, BOOL isEndTransaction);
FT4222_SPIMaster_SingleRead.argtypes = [
    FT_HANDLE, POINTER(BYTE), WORD,
    POINTER(WORD), BOOL
]
FT4222_SPIMaster_SingleRead.__doc__ = \
    """FT4222_STATUS FT4222_SPIMaster_SingleRead(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeOfRead, BOOL isEndTransaction);
ftd2xx.h:264"""

# LibFT4222.h 265
FT4222_SPIMaster_SingleWrite = ft4222.FT4222_SPIMaster_SingleWrite
FT4222_SPIMaster_SingleWrite.restype = FT_STATUS
# FT4222_STATUS FT4222_SPIMaster_SingleWrite(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred, BOOL isEndTransaction);
FT4222_SPIMaster_SingleWrite.argtypes = [
    FT_HANDLE, POINTER(BYTE), WORD,
    POINTER(WORD), BOOL
]
FT4222_SPIMaster_SingleWrite.__doc__ = \
    """FT4222_STATUS FT4222_SPIMaster_SingleWrite(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred, BOOL isEndTransaction);
ftd2xx.h:265"""

# LibFT4222.h 266
FT4222_SPIMaster_SingleReadWrite = ft4222.FT4222_SPIMaster_SingleReadWrite
FT4222_SPIMaster_SingleReadWrite.restype = FT_STATUS
# FT4222_STATUS FT4222_SPIMaster_SingleReadWrite(FT_HANDLE ftHandle, uint8* readBuffer, uint8* writeBuffer, uint16 bufferSize, uint16* sizeTransferred, BOOL isEndTransaction);
FT4222_SPIMaster_SingleReadWrite.argtypes = [
    FT_HANDLE,
    POINTER(BYTE),
    POINTER(BYTE), WORD,
    POINTER(WORD), BOOL
]
FT4222_SPIMaster_SingleReadWrite.__doc__ = \
    """FT4222_STATUS FT4222_SPIMaster_SingleReadWrite(FT_HANDLE ftHandle, uint8* readBuffer, uint8* writeBuffer, uint16 bufferSize, uint16* sizeTransferred, BOOL isEndTransaction);
ftd2xx.h:266"""

# LibFT4222.h 267
FT4222_SPIMaster_MultiReadWrite = ft4222.FT4222_SPIMaster_MultiReadWrite
FT4222_SPIMaster_MultiReadWrite.restype = FT_STATUS
# FT4222_STATUS FT4222_SPIMaster_MultiReadWrite(FT_HANDLE ftHandle, uint8* readBuffer, uint8* writeBuffer, uint8 singleWriteBytes, uint16 multiWriteBytes, uint16 multiReadBytes, uint32* sizeOfRead);
FT4222_SPIMaster_MultiReadWrite.argtypes = [
    FT_HANDLE,
    POINTER(BYTE),
    POINTER(BYTE), BYTE, WORD, WORD,
    POINTER(DWORD)
]
FT4222_SPIMaster_MultiReadWrite.__doc__ = \
    """FT4222_STATUS FT4222_SPIMaster_MultiReadWrite(FT_HANDLE ftHandle, uint8* readBuffer, uint8* writeBuffer, uint8 singleWriteBytes, uint16 multiWriteBytes, uint16 multiReadBytes, uint32* sizeOfRead);
ftd2xx.h:267"""

# LibFT4222.h 269
FT4222_SPISlave_Init = ft4222.FT4222_SPISlave_Init
FT4222_SPISlave_Init.restype = FT_STATUS
# FT4222_STATUS FT4222_SPISlave_Init(FT_HANDLE ftHandle);
FT4222_SPISlave_Init.argtypes = [FT_HANDLE]
FT4222_SPISlave_Init.__doc__ = \
    """FT4222_STATUS FT4222_SPISlave_Init(FT_HANDLE ftHandle);
ftd2xx.h:269"""

# LibFT4222.h 270
FT4222_SPISlave_GetRxStatus = ft4222.FT4222_SPISlave_GetRxStatus
FT4222_SPISlave_GetRxStatus.restype = FT_STATUS
# FT4222_STATUS FT4222_SPISlave_GetRxStatus(FT_HANDLE ftHandle, uint16* pRxSize);
FT4222_SPISlave_GetRxStatus.argtypes = [FT_HANDLE, POINTER(WORD)]
FT4222_SPISlave_GetRxStatus.__doc__ = \
    """FT4222_STATUS FT4222_SPISlave_GetRxStatus(FT_HANDLE ftHandle, uint16* pRxSize);
ftd2xx.h:270"""

# LibFT4222.h 271
FT4222_SPISlave_Read = ft4222.FT4222_SPISlave_Read
FT4222_SPISlave_Read.restype = FT_STATUS
# FT4222_STATUS FT4222_SPISlave_Read(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeOfRead);
FT4222_SPISlave_Read.argtypes = [FT_HANDLE, POINTER(BYTE), WORD, POINTER(WORD)]
FT4222_SPISlave_Read.__doc__ = \
    """FT4222_STATUS FT4222_SPISlave_Read(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeOfRead);
ftd2xx.h:271"""

# LibFT4222.h 272
FT4222_SPISlave_Write = ft4222.FT4222_SPISlave_Write
FT4222_SPISlave_Write.restype = FT_STATUS
# FT4222_STATUS FT4222_SPISlave_Write(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
FT4222_SPISlave_Write.argtypes = [
    FT_HANDLE, POINTER(BYTE), WORD,
    POINTER(WORD)
]
FT4222_SPISlave_Write.__doc__ = \
    """FT4222_STATUS FT4222_SPISlave_Write(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
ftd2xx.h:272"""

# LibFT4222.h 274
FT4222_SPI_Reset = ft4222.FT4222_SPI_Reset
FT4222_SPI_Reset.restype = FT_STATUS
# FT4222_STATUS FT4222_SPI_Reset(FT_HANDLE ftHandle);
FT4222_SPI_Reset.argtypes = [FT_HANDLE]
FT4222_SPI_Reset.__doc__ = \
    """FT4222_STATUS FT4222_SPI_Reset(FT_HANDLE ftHandle);
ftd2xx.h:274"""

# LibFT4222.h 275
FT4222_SPI_ResetTransaction = ft4222.FT4222_SPI_ResetTransaction
FT4222_SPI_ResetTransaction.restype = FT_STATUS
# FT4222_STATUS FT4222_SPI_ResetTransaction(FT_HANDLE ftHandle, uint8 spiIdx);
FT4222_SPI_ResetTransaction.argtypes = [FT_HANDLE, BYTE]
FT4222_SPI_ResetTransaction.__doc__ = \
    """FT4222_STATUS FT4222_SPI_ResetTransaction(FT_HANDLE ftHandle, uint8 spiIdx);
ftd2xx.h:275"""

# LibFT4222.h 276
FT4222_SPI_SetDrivingStrenght = ft4222.FT4222_SPI_SetDrivingStrength
FT4222_SPI_SetDrivingStrenght.restype = FT_STATUS
# FT4222_STATUS FT4222_SPI_SetDrivingStrength(FT_HANDLE ftHandle, SPI_DrivingStrength clkStrength, SPI_DrivingStrength ioStrength, SPI_DrivingStrength ssoStregth);
FT4222_SPI_SetDrivingStrenght.argtypes = [FT_HANDLE, DWORD, DWORD, DWORD]
FT4222_SPI_SetDrivingStrenght.__doc__ = \
    """FT4222_STATUS FT4222_SPI_SetDrivingStrength(FT_HANDLE ftHandle, SPI_DrivingStrength clkStrength, SPI_DrivingStrength ioStrength, SPI_DrivingStrength ssoStregth);
ftd2xx.h:276"""

# FT4222 I2C Functions
# LibFT4222.h 281
FT4222_I2CMaster_Init = ft4222.FT4222_I2CMaster_Init
FT4222_I2CMaster_Init.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CMaster_Init(FT_HANDLE ftHandle, uint32 kbps);
FT4222_I2CMaster_Init.argtypes = [FT_HANDLE, DWORD]
FT4222_I2CMaster_Init.__doc__ = \
    """FT4222_STATUS FT4222_I2CMaster_Init(FT_HANDLE ftHandle, uint32 kbps);
ftd2xx.h:281"""

# LibFT4222.h 282
FT4222_I2CMaster_Read = ft4222.FT4222_I2CMaster_Read
FT4222_I2CMaster_Read.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CMaster_Read(FT_HANDLE ftHandle, uint16 deviceAddress, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
FT4222_I2CMaster_Read.argtypes = [
    FT_HANDLE, WORD, POINTER(BYTE), WORD,
    POINTER(WORD)
]
FT4222_I2CMaster_Read.__doc__ = \
    """FT4222_STATUS FT4222_I2CMaster_Read(FT_HANDLE ftHandle, uint16 deviceAddress, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
ftd2xx.h:282"""

# LibFT4222.h 283
FT4222_I2CMaster_Write = ft4222.FT4222_I2CMaster_Write
FT4222_I2CMaster_Write.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CMaster_Write(FT_HANDLE ftHandle, uint16 deviceAddress, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
FT4222_I2CMaster_Write.argtypes = [
    FT_HANDLE, WORD, POINTER(BYTE), WORD,
    POINTER(WORD)
]
FT4222_I2CMaster_Write.__doc__ = \
    """FT4222_STATUS FT4222_I2CMaster_Write(FT_HANDLE ftHandle, uint16 deviceAddress, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
ftd2xx.h:283"""

# LibFT4222.h 284
FT4222_I2CMaster_Reset = ft4222.FT4222_I2CMaster_Reset
FT4222_I2CMaster_Reset.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CMaster_Reset(FT_HANDLE ftHandle);
FT4222_I2CMaster_Reset.argtypes = [FT_HANDLE]
FT4222_I2CMaster_Reset.__doc__ = \
    """FT4222_STATUS FT4222_I2CMaster_Reset(FT_HANDLE ftHandle);
ftd2xx.h:264"""

# LibFT4222.h 286
FT4222_I2CSlave_Init = ft4222.FT4222_I2CSlave_Init
FT4222_I2CSlave_Init.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CSlave_Init(FT_HANDLE ftHandle);
FT4222_I2CSlave_Init.argtypes = [FT_HANDLE]
FT4222_I2CSlave_Init.__doc__ = \
    """FT4222_STATUS FT4222_I2CSlave_Init(FT_HANDLE ftHandle);
ftd2xx.h:286"""

# LibFT4222.h 287
FT4222_I2CSlave_Reset = ft4222.FT4222_I2CSlave_Reset
FT4222_I2CSlave_Reset.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CSlave_Reset(FT_HANDLE ftHandle);
FT4222_I2CSlave_Reset.argtypes = [FT_HANDLE]
FT4222_I2CSlave_Reset.__doc__ = \
    """FT4222_STATUS FT4222_I2CSlave_Reset(FT_HANDLE ftHandle);
ftd2xx.h:287"""

# LibFT4222.h 288
FT4222_I2CSlave_GetAddress = ft4222.FT4222_I2CSlave_GetAddress
FT4222_I2CSlave_GetAddress.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CSlave_GetAddress(FT_HANDLE ftHandle, uint8* addr);
FT4222_I2CSlave_GetAddress.argtypes = [FT_HANDLE, POINTER(BYTE)]
FT4222_I2CSlave_GetAddress.__doc__ = \
    """FT4222_STATUS FT4222_I2CSlave_GetAddress(FT_HANDLE ftHandle, uint8* addr);
ftd2xx.h:288"""

# LibFT4222.h 289
FT4222_I2CSlave_SetAddress = ft4222.FT4222_I2CSlave_SetAddress
FT4222_I2CSlave_SetAddress.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CSlave_SetAddress(FT_HANDLE ftHandle, uint8 addr);
FT4222_I2CSlave_SetAddress.argtypes = [FT_HANDLE, BYTE]
FT4222_I2CSlave_SetAddress.__doc__ = \
    """FT4222_STATUS FT4222_I2CSlave_SetAddress(FT_HANDLE ftHandle, uint8 addr);
ftd2xx.h:289"""

# LibFT4222.h 290
FT4222_I2CSlave_GetRxStatus = ft4222.FT4222_I2CSlave_GetRxStatus
FT4222_I2CSlave_GetRxStatus.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CSlave_GetRxStatus(FT_HANDLE ftHandle, uint16* pRxSize);
FT4222_I2CSlave_GetRxStatus.argtypes = [FT_HANDLE, POINTER(WORD)]
FT4222_I2CSlave_GetRxStatus.__doc__ = \
    """FT4222_STATUS FT4222_I2CSlave_GetRxStatus(FT_HANDLE ftHandle, uint16* pRxSize);
ftd2xx.h:290"""

# LibFT4222.h 291
FT4222_I2CSlave_Read = ft4222.FT4222_I2CSlave_Read
FT4222_I2CSlave_Read.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CSlave_Read(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
FT4222_I2CSlave_Read.argtypes = [FT_HANDLE, POINTER(BYTE), WORD, POINTER(WORD)]
FT4222_I2CSlave_Read.__doc__ = \
    """FT4222_STATUS FT4222_I2CSlave_Read(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
ftd2xx.h:291"""

# LibFT4222.h 292
FT4222_I2CSlave_Write = ft4222.FT4222_I2CSlave_Write
FT4222_I2CSlave_Write.restype = FT_STATUS
# FT4222_STATUS FT4222_I2CSlave_Write(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
FT4222_I2CSlave_Write.argtypes = [
    FT_HANDLE, POINTER(BYTE), WORD,
    POINTER(WORD)
]
FT4222_I2CSlave_Write.__doc__ = \
    """FT4222_STATUS FT4222_I2CSlave_Write(FT_HANDLE ftHandle, uint8* buffer, uint16 bufferSize, uint16* sizeTransferred);
ftd2xx.h:292"""

# FT4222 GPIO Functions
# LibFT4222.h 297
FT4222_GPIO_Init = ft4222.FT4222_GPIO_Init
FT4222_GPIO_Init.restype = FT_STATUS
# FT4222_STATUS FT4222_GPIO_Init(FT_HANDLE ftHandle, GPIO_Dir gpioDir[4]);
FT4222_GPIO_Init.argtypes = [FT_HANDLE, POINTER(DWORD)]
FT4222_GPIO_Init.__doc__ = \
    """FT4222_STATUS FT4222_GPIO_Init(FT_HANDLE ftHandle, GPIO_Dir gpioDir[4]);
ftd2xx.h:297"""

# LibFT4222.h 298
FT4222_GPIO_Read = ft4222.FT4222_GPIO_Read
FT4222_GPIO_Read.restype = FT_STATUS
# FT4222_STATUS FT4222_GPIO_Read(FT_HANDLE ftHandle, GPIO_Port portNum, BOOL* value);
FT4222_GPIO_Read.argtypes = [FT_HANDLE, DWORD, POINTER(BOOL)]
FT4222_GPIO_Read.__doc__ = \
    """FT4222_STATUS FT4222_GPIO_Read(FT_HANDLE ftHandle, GPIO_Port portNum, BOOL* value);
ftd2xx.h:298"""

# LibFT4222.h 299
FT4222_GPIO_Write = ft4222.FT4222_GPIO_Write
FT4222_GPIO_Write.restype = FT_STATUS
# FT4222_STATUS FT4222_GPIO_Write(FT_HANDLE ftHandle, GPIO_Port portNum, BOOL bValue);
FT4222_GPIO_Write.argtypes = [FT_HANDLE, DWORD, BOOL]
FT4222_GPIO_Write.__doc__ = \
    """FT4222_STATUS FT4222_GPIO_Write(FT_HANDLE ftHandle, GPIO_Port portNum, BOOL bValue);
ftd2xx.h:299"""

# LibFT4222.h 300
FT4222_GPIO_SetInputTrigger = ft4222.FT4222_GPIO_SetInputTrigger
FT4222_GPIO_SetInputTrigger.restype = FT_STATUS
# FT4222_STATUS FT4222_GPIO_SetInputTrigger(FT_HANDLE ftHandle, GPIO_Port portNum, GPIO_Tigger trigger);
FT4222_GPIO_SetInputTrigger.argtypes = [FT_HANDLE, DWORD, DWORD]
FT4222_GPIO_SetInputTrigger.__doc__ = \
    """FT4222_STATUS FT4222_GPIO_SetInputTrigger(FT_HANDLE ftHandle, GPIO_Port portNum, GPIO_Tigger trigger);
ftd2xx.h:300"""

# LibFT4222.h 301
FT4222_GPIO_GetTriggerStatus = ft4222.FT4222_GPIO_GetTriggerStatus
FT4222_GPIO_GetTriggerStatus.restype = FT_STATUS
# FT4222_STATUS FT4222_GPIO_GetTriggerStatus(FT_HANDLE ftHandle, GPIO_Port portNum, uint16* queueSize);
FT4222_GPIO_GetTriggerStatus.argtypes = [FT_HANDLE, DWORD, POINTER(WORD)]
FT4222_GPIO_GetTriggerStatus.__doc__ = \
    """FT4222_STATUS FT4222_GPIO_GetTriggerStatus(FT_HANDLE ftHandle, GPIO_Port portNum, uint16* queueSize);
ftd2xx.h:301"""

# LibFT4222.h 302
FT4222_GPIO_ReadTriggerQueue = ft4222.FT4222_GPIO_ReadTriggerQueue
FT4222_GPIO_ReadTriggerQueue.restype = FT_STATUS
# FT4222_STATUS FT4222_GPIO_ReadTriggerQueue(FT_HANDLE ftHandle, GPIO_Port portNum, GPIO_Tigger* events, uint16 readSize, uint16* sizeofRead);
FT4222_GPIO_ReadTriggerQueue.argtypes = [
    FT_HANDLE, DWORD, POINTER(DWORD), WORD,
    POINTER(WORD)
]
FT4222_GPIO_ReadTriggerQueue.__doc__ = \
    """FT4222_STATUS FT4222_GPIO_ReadTriggerQueue(FT_HANDLE ftHandle, GPIO_Port portNum, GPIO_Tigger* events, uint16 readSize, uint16* sizeofRead);
ftd2xx.h:302"""
