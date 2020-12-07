# generated by 'xml2py'
# flags '-c -d -k defst -l ftd2xx.dll -o _ftd2xx.py -m ctypes.wintypes ftd2xx.xml'
import sys
from ctypes import *
from ctypes.util import find_library


STRING = c_char_p
if sys.platform == 'win32':
    from ctypes.wintypes import DWORD
    from ctypes.wintypes import ULONG
    from ctypes.wintypes import WORD
    from ctypes.wintypes import BYTE
    from ctypes.wintypes import BOOL
    from ctypes.wintypes import BOOLEAN
    from ctypes.wintypes import LPCSTR
    from ctypes.wintypes import HANDLE
    from ctypes.wintypes import LONG
    from ctypes.wintypes import UINT
    from ctypes.wintypes import LPSTR
    from ctypes.wintypes import FILETIME
else:
    DWORD = c_ulong
    ULONG = c_ulong
    WORD = c_ushort
    BYTE = c_ubyte
    BOOL = c_int
    BOOLEAN = c_char
    LPCSTR = STRING
    HANDLE = c_void_p
    LONG = c_long
    UINT = c_uint
    LPSTR = STRING

_libraries = {}

if sys.platform == 'win32':
    try:
        _libraries['ftd2xx.dll'] = WinDLL('ftd2xx64.dll')
    except OSError: # 32-bit, or 64-bit library with plain name
        try:
            _libraries['ftd2xx.dll'] = WinDLL('ftd2xx.dll')
        except OSError as e:
            if e.winerror == 126:
                error_message = e.args[1] + 'Unable to find D2XX DLL. Please make sure ftd2xx.dll or ftd2xx64.dll is in the path.'
                e.args = (e.args[0], error_message) + e.args[2:]
                raise e
            else:
                raise
else:
    _libraries['ftd2xx.dll'] = CDLL('libftd2xx.so')


FT_DEVICE_2232C = 4
FT_OTHER_ERROR = 18
FT_DEVICE_NOT_OPENED = 3
FT_NOT_SUPPORTED = 17
FT_INVALID_BAUD_RATE = 7
FT_DEVICE_NOT_OPENED_FOR_ERASE = 8
FT_EEPROM_NOT_PRESENT = 14
FT_DEVICE_232R = 5
FT_DEVICE_AM = 1
FT_DEVICE_BM = 0
FT_DEVICE_100AX = 2
FT_EEPROM_WRITE_FAILED = 12
FT_IO_ERROR = 4
FT_DEVICE_NOT_OPENED_FOR_WRITE = 9
FT_INVALID_HANDLE = 1
FT_EEPROM_ERASE_FAILED = 13
FT_EEPROM_READ_FAILED = 11
FT_INSUFFICIENT_RESOURCES = 5
FT_DEVICE_UNKNOWN = 3
FT_INVALID_ARGS = 16
FT_FAILED_TO_WRITE_DEVICE = 10
FT_DEVICE_NOT_FOUND = 2
FT_EEPROM_NOT_PROGRAMMED = 15
FT_OK = 0
FT_INVALID_PARAMETER = 6
USHORT = c_ushort
SHORT = c_short
UCHAR = c_ubyte
LPBYTE = POINTER(c_ubyte)
CHAR = c_char
LPBOOL = POINTER(c_int)
PUCHAR = POINTER(c_ubyte)
PCHAR = STRING
PVOID = c_void_p
INT = c_int
LPTSTR = STRING
LPDWORD = POINTER(DWORD)
LPWORD = POINTER(WORD)
LPLONG = POINTER(LONG)
PULONG = POINTER(ULONG)
LPVOID = PVOID
VOID = None
ULONGLONG = c_ulonglong
# WinTypes.h 38
class _OVERLAPPED(Structure):
    pass
_OVERLAPPED._fields_ = [
    # WinTypes.h 38
    ('Internal', DWORD),
    ('InternalHigh', DWORD),
    ('Offset', DWORD),
    ('OffsetHigh', DWORD),
    ('hEvent', HANDLE),
]
LPOVERLAPPED = POINTER(_OVERLAPPED)
OVERLAPPED = _OVERLAPPED
# WinTypes.h 46
class _SECURITY_ATTRIBUTES(Structure):
    pass
_SECURITY_ATTRIBUTES._fields_ = [
    # WinTypes.h 46
    ('nLength', DWORD),
    ('lpSecurityDescriptor', LPVOID),
    ('bInheritHandle', BOOL),
]
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)
SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES
# WinTypes.h 52
class timeval(Structure):
    pass
timeval._fields_ = [
    # WinTypes.h 52
]
SYSTEMTIME = timeval
FT_HANDLE = PVOID
FT_STATUS = ULONG

# values for unnamed enumeration
PFT_EVENT_HANDLER = CFUNCTYPE(None, c_ulong, c_ulong)
FT_DEVICE = ULONG

# values for unnamed enumeration
# ftd2xx.h 216
FT_Open = _libraries['ftd2xx.dll'].FT_Open
FT_Open.restype = FT_STATUS
# FT_Open(deviceNumber, pHandle)
FT_Open.argtypes = [c_int, POINTER(FT_HANDLE)]
FT_Open.__doc__ = \
"""FT_STATUS FT_Open(int deviceNumber, FT_HANDLE * pHandle)
ftd2xx.h:216"""
# ftd2xx.h 223
FT_OpenEx = _libraries['ftd2xx.dll'].FT_OpenEx
FT_OpenEx.restype = FT_STATUS
# FT_OpenEx(pArg1, Flags, pHandle)
FT_OpenEx.argtypes = [PVOID, DWORD, POINTER(FT_HANDLE)]
FT_OpenEx.__doc__ = \
"""FT_STATUS FT_OpenEx(PVOID pArg1, DWORD Flags, FT_HANDLE * pHandle)
ftd2xx.h:223"""
# ftd2xx.h 230
FT_ListDevices = _libraries['ftd2xx.dll'].FT_ListDevices
FT_ListDevices.restype = FT_STATUS
# FT_ListDevices(pArg1, pArg2, Flags)
FT_ListDevices.argtypes = [PVOID, PVOID, DWORD]
FT_ListDevices.__doc__ = \
"""FT_STATUS FT_ListDevices(PVOID pArg1, PVOID pArg2, DWORD Flags)
ftd2xx.h:230"""
# ftd2xx.h 235
FT_Close = _libraries['ftd2xx.dll'].FT_Close
FT_Close.restype = FT_STATUS
# FT_Close(ftHandle)
FT_Close.argtypes = [FT_HANDLE]
FT_Close.__doc__ = \
"""FT_STATUS FT_Close(FT_HANDLE ftHandle)
ftd2xx.h:235"""
# ftd2xx.h 243
FT_Read = _libraries['ftd2xx.dll'].FT_Read
FT_Read.restype = FT_STATUS
# FT_Read(ftHandle, lpBuffer, nBufferSize, lpBytesReturned)
FT_Read.argtypes = [FT_HANDLE, LPVOID, DWORD, LPDWORD]
FT_Read.__doc__ = \
"""FT_STATUS FT_Read(FT_HANDLE ftHandle, LPVOID lpBuffer, DWORD nBufferSize, LPDWORD lpBytesReturned)
ftd2xx.h:243"""
# ftd2xx.h 251
FT_Write = _libraries['ftd2xx.dll'].FT_Write
FT_Write.restype = FT_STATUS
# FT_Write(ftHandle, lpBuffer, nBufferSize, lpBytesWritten)
FT_Write.argtypes = [FT_HANDLE, LPVOID, DWORD, LPDWORD]
FT_Write.__doc__ = \
"""FT_STATUS FT_Write(FT_HANDLE ftHandle, LPVOID lpBuffer, DWORD nBufferSize, LPDWORD lpBytesWritten)
ftd2xx.h:251"""
# ftd2xx.h 263
FT_IoCtl = _libraries['ftd2xx.dll'].FT_IoCtl
FT_IoCtl.restype = FT_STATUS
# FT_IoCtl(ftHandle, dwIoControlCode, lpInBuf, nInBufSize, lpOutBuf, nOutBufSize, lpBytesReturned, lpOverlapped)
FT_IoCtl.argtypes = [FT_HANDLE, DWORD, LPVOID, DWORD, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
FT_IoCtl.__doc__ = \
"""FT_STATUS FT_IoCtl(FT_HANDLE ftHandle, DWORD dwIoControlCode, LPVOID lpInBuf, DWORD nInBufSize, LPVOID lpOutBuf, DWORD nOutBufSize, LPDWORD lpBytesReturned, LPOVERLAPPED lpOverlapped)
ftd2xx.h:263"""
# ftd2xx.h 269
FT_SetBaudRate = _libraries['ftd2xx.dll'].FT_SetBaudRate
FT_SetBaudRate.restype = FT_STATUS
# FT_SetBaudRate(ftHandle, BaudRate)
FT_SetBaudRate.argtypes = [FT_HANDLE, ULONG]
FT_SetBaudRate.__doc__ = \
"""FT_STATUS FT_SetBaudRate(FT_HANDLE ftHandle, ULONG BaudRate)
ftd2xx.h:269"""
# ftd2xx.h 275
FT_SetDivisor = _libraries['ftd2xx.dll'].FT_SetDivisor
FT_SetDivisor.restype = FT_STATUS
# FT_SetDivisor(ftHandle, Divisor)
FT_SetDivisor.argtypes = [FT_HANDLE, USHORT]
FT_SetDivisor.__doc__ = \
"""FT_STATUS FT_SetDivisor(FT_HANDLE ftHandle, USHORT Divisor)
ftd2xx.h:275"""
# ftd2xx.h 283
FT_SetDataCharacteristics = _libraries['ftd2xx.dll'].FT_SetDataCharacteristics
FT_SetDataCharacteristics.restype = FT_STATUS
# FT_SetDataCharacteristics(ftHandle, WordLength, StopBits, Parity)
FT_SetDataCharacteristics.argtypes = [FT_HANDLE, UCHAR, UCHAR, UCHAR]
FT_SetDataCharacteristics.__doc__ = \
"""FT_STATUS FT_SetDataCharacteristics(FT_HANDLE ftHandle, UCHAR WordLength, UCHAR StopBits, UCHAR Parity)
ftd2xx.h:283"""
# ftd2xx.h 291
FT_SetFlowControl = _libraries['ftd2xx.dll'].FT_SetFlowControl
FT_SetFlowControl.restype = FT_STATUS
# FT_SetFlowControl(ftHandle, FlowControl, XonChar, XoffChar)
FT_SetFlowControl.argtypes = [FT_HANDLE, USHORT, UCHAR, UCHAR]
FT_SetFlowControl.__doc__ = \
"""FT_STATUS FT_SetFlowControl(FT_HANDLE ftHandle, USHORT FlowControl, UCHAR XonChar, UCHAR XoffChar)
ftd2xx.h:291"""
# ftd2xx.h 296
FT_ResetDevice = _libraries['ftd2xx.dll'].FT_ResetDevice
FT_ResetDevice.restype = FT_STATUS
# FT_ResetDevice(ftHandle)
FT_ResetDevice.argtypes = [FT_HANDLE]
FT_ResetDevice.__doc__ = \
"""FT_STATUS FT_ResetDevice(FT_HANDLE ftHandle)
ftd2xx.h:296"""
# ftd2xx.h 301
FT_SetDtr = _libraries['ftd2xx.dll'].FT_SetDtr
FT_SetDtr.restype = FT_STATUS
# FT_SetDtr(ftHandle)
FT_SetDtr.argtypes = [FT_HANDLE]
FT_SetDtr.__doc__ = \
"""FT_STATUS FT_SetDtr(FT_HANDLE ftHandle)
ftd2xx.h:301"""
# ftd2xx.h 306
FT_ClrDtr = _libraries['ftd2xx.dll'].FT_ClrDtr
FT_ClrDtr.restype = FT_STATUS
# FT_ClrDtr(ftHandle)
FT_ClrDtr.argtypes = [FT_HANDLE]
FT_ClrDtr.__doc__ = \
"""FT_STATUS FT_ClrDtr(FT_HANDLE ftHandle)
ftd2xx.h:306"""
# ftd2xx.h 311
FT_SetRts = _libraries['ftd2xx.dll'].FT_SetRts
FT_SetRts.restype = FT_STATUS
# FT_SetRts(ftHandle)
FT_SetRts.argtypes = [FT_HANDLE]
FT_SetRts.__doc__ = \
"""FT_STATUS FT_SetRts(FT_HANDLE ftHandle)
ftd2xx.h:311"""
# ftd2xx.h 316
FT_ClrRts = _libraries['ftd2xx.dll'].FT_ClrRts
FT_ClrRts.restype = FT_STATUS
# FT_ClrRts(ftHandle)
FT_ClrRts.argtypes = [FT_HANDLE]
FT_ClrRts.__doc__ = \
"""FT_STATUS FT_ClrRts(FT_HANDLE ftHandle)
ftd2xx.h:316"""
# ftd2xx.h 322
FT_GetModemStatus = _libraries['ftd2xx.dll'].FT_GetModemStatus
FT_GetModemStatus.restype = FT_STATUS
# FT_GetModemStatus(ftHandle, pModemStatus)
FT_GetModemStatus.argtypes = [FT_HANDLE, POINTER(ULONG)]
FT_GetModemStatus.__doc__ = \
"""FT_STATUS FT_GetModemStatus(FT_HANDLE ftHandle, ULONG * pModemStatus)
ftd2xx.h:322"""
# ftd2xx.h 331
FT_SetChars = _libraries['ftd2xx.dll'].FT_SetChars
FT_SetChars.restype = FT_STATUS
# FT_SetChars(ftHandle, EventChar, EventCharEnabled, ErrorChar, ErrorCharEnabled)
FT_SetChars.argtypes = [FT_HANDLE, UCHAR, UCHAR, UCHAR, UCHAR]
FT_SetChars.__doc__ = \
"""FT_STATUS FT_SetChars(FT_HANDLE ftHandle, UCHAR EventChar, UCHAR EventCharEnabled, UCHAR ErrorChar, UCHAR ErrorCharEnabled)
ftd2xx.h:331"""
# ftd2xx.h 337
FT_Purge = _libraries['ftd2xx.dll'].FT_Purge
FT_Purge.restype = FT_STATUS
# FT_Purge(ftHandle, Mask)
FT_Purge.argtypes = [FT_HANDLE, ULONG]
FT_Purge.__doc__ = \
"""FT_STATUS FT_Purge(FT_HANDLE ftHandle, ULONG Mask)
ftd2xx.h:337"""
# ftd2xx.h 344
FT_SetTimeouts = _libraries['ftd2xx.dll'].FT_SetTimeouts
FT_SetTimeouts.restype = FT_STATUS
# FT_SetTimeouts(ftHandle, ReadTimeout, WriteTimeout)
FT_SetTimeouts.argtypes = [FT_HANDLE, ULONG, ULONG]
FT_SetTimeouts.__doc__ = \
"""FT_STATUS FT_SetTimeouts(FT_HANDLE ftHandle, ULONG ReadTimeout, ULONG WriteTimeout)
ftd2xx.h:344"""
# ftd2xx.h 350
FT_GetQueueStatus = _libraries['ftd2xx.dll'].FT_GetQueueStatus
FT_GetQueueStatus.restype = FT_STATUS
# FT_GetQueueStatus(ftHandle, dwRxBytes)
FT_GetQueueStatus.argtypes = [FT_HANDLE, POINTER(DWORD)]
FT_GetQueueStatus.__doc__ = \
"""FT_STATUS FT_GetQueueStatus(FT_HANDLE ftHandle, DWORD * dwRxBytes)
ftd2xx.h:350"""
# ftd2xx.h 357
FT_SetEventNotification = _libraries['ftd2xx.dll'].FT_SetEventNotification
FT_SetEventNotification.restype = FT_STATUS
# FT_SetEventNotification(ftHandle, Mask, Param)
FT_SetEventNotification.argtypes = [FT_HANDLE, DWORD, PVOID]
FT_SetEventNotification.__doc__ = \
"""FT_STATUS FT_SetEventNotification(FT_HANDLE ftHandle, DWORD Mask, PVOID Param)
ftd2xx.h:357"""
# ftd2xx.h 365
FT_GetStatus = _libraries['ftd2xx.dll'].FT_GetStatus
FT_GetStatus.restype = FT_STATUS
# FT_GetStatus(ftHandle, dwRxBytes, dwTxBytes, dwEventDWord)
FT_GetStatus.argtypes = [FT_HANDLE, POINTER(DWORD), POINTER(DWORD), POINTER(DWORD)]
FT_GetStatus.__doc__ = \
"""FT_STATUS FT_GetStatus(FT_HANDLE ftHandle, DWORD * dwRxBytes, DWORD * dwTxBytes, DWORD * dwEventDWord)
ftd2xx.h:365"""
# ftd2xx.h 370
FT_SetBreakOn = _libraries['ftd2xx.dll'].FT_SetBreakOn
FT_SetBreakOn.restype = FT_STATUS
# FT_SetBreakOn(ftHandle)
FT_SetBreakOn.argtypes = [FT_HANDLE]
FT_SetBreakOn.__doc__ = \
"""FT_STATUS FT_SetBreakOn(FT_HANDLE ftHandle)
ftd2xx.h:370"""
# ftd2xx.h 375
FT_SetBreakOff = _libraries['ftd2xx.dll'].FT_SetBreakOff
FT_SetBreakOff.restype = FT_STATUS
# FT_SetBreakOff(ftHandle)
FT_SetBreakOff.argtypes = [FT_HANDLE]
FT_SetBreakOff.__doc__ = \
"""FT_STATUS FT_SetBreakOff(FT_HANDLE ftHandle)
ftd2xx.h:375"""
# ftd2xx.h 381
FT_SetWaitMask = _libraries['ftd2xx.dll'].FT_SetWaitMask
FT_SetWaitMask.restype = FT_STATUS
# FT_SetWaitMask(ftHandle, Mask)
FT_SetWaitMask.argtypes = [FT_HANDLE, DWORD]
FT_SetWaitMask.__doc__ = \
"""FT_STATUS FT_SetWaitMask(FT_HANDLE ftHandle, DWORD Mask)
ftd2xx.h:381"""
# ftd2xx.h 387
FT_WaitOnMask = _libraries['ftd2xx.dll'].FT_WaitOnMask
FT_WaitOnMask.restype = FT_STATUS
# FT_WaitOnMask(ftHandle, Mask)
FT_WaitOnMask.argtypes = [FT_HANDLE, POINTER(DWORD)]
FT_WaitOnMask.__doc__ = \
"""FT_STATUS FT_WaitOnMask(FT_HANDLE ftHandle, DWORD * Mask)
ftd2xx.h:387"""
# ftd2xx.h 393
FT_GetEventStatus = _libraries['ftd2xx.dll'].FT_GetEventStatus
FT_GetEventStatus.restype = FT_STATUS
# FT_GetEventStatus(ftHandle, dwEventDWord)
FT_GetEventStatus.argtypes = [FT_HANDLE, POINTER(DWORD)]
FT_GetEventStatus.__doc__ = \
"""FT_STATUS FT_GetEventStatus(FT_HANDLE ftHandle, DWORD * dwEventDWord)
ftd2xx.h:393"""
# ftd2xx.h 400
FT_ReadEE = _libraries['ftd2xx.dll'].FT_ReadEE
FT_ReadEE.restype = FT_STATUS
# FT_ReadEE(ftHandle, dwWordOffset, lpwValue)
FT_ReadEE.argtypes = [FT_HANDLE, DWORD, LPWORD]
FT_ReadEE.__doc__ = \
"""FT_STATUS FT_ReadEE(FT_HANDLE ftHandle, DWORD dwWordOffset, LPWORD lpwValue)
ftd2xx.h:400"""
# ftd2xx.h 407
FT_WriteEE = _libraries['ftd2xx.dll'].FT_WriteEE
FT_WriteEE.restype = FT_STATUS
# FT_WriteEE(ftHandle, dwWordOffset, wValue)
FT_WriteEE.argtypes = [FT_HANDLE, DWORD, WORD]
FT_WriteEE.__doc__ = \
"""FT_STATUS FT_WriteEE(FT_HANDLE ftHandle, DWORD dwWordOffset, WORD wValue)
ftd2xx.h:407"""
# ftd2xx.h 412
FT_EraseEE = _libraries['ftd2xx.dll'].FT_EraseEE
FT_EraseEE.restype = FT_STATUS
# FT_EraseEE(ftHandle)
FT_EraseEE.argtypes = [FT_HANDLE]
FT_EraseEE.__doc__ = \
"""FT_STATUS FT_EraseEE(FT_HANDLE ftHandle)
ftd2xx.h:412"""
# ftd2xx.h 417
class ft_program_data(Structure):
    pass
ft_program_data._fields_ = [
    # ftd2xx.h 417
    ('Signature1', DWORD),
    ('Signature2', DWORD),
    ('Version', DWORD),
    ('VendorId', WORD),
    ('ProductId', WORD),
    ('Manufacturer', STRING),
    ('ManufacturerId', STRING),
    ('Description', STRING),
    ('SerialNumber', STRING),
    ('MaxPower', WORD),
    ('PnP', WORD),
    ('SelfPowered', WORD),
    ('RemoteWakeup', WORD),
    ('Rev4', UCHAR),
    ('IsoIn', UCHAR),
    ('IsoOut', UCHAR),
    ('PullDownEnable', UCHAR),
    ('SerNumEnable', UCHAR),
    ('USBVersionEnable', UCHAR),
    ('USBVersion', WORD),
    ('Rev5', UCHAR),
    ('IsoInA', UCHAR),
    ('IsoInB', UCHAR),
    ('IsoOutA', UCHAR),
    ('IsoOutB', UCHAR),
    ('PullDownEnable5', UCHAR),
    ('SerNumEnable5', UCHAR),
    ('USBVersionEnable5', UCHAR),
    ('USBVersion5', WORD),
    ('AIsHighCurrent', UCHAR),
    ('BIsHighCurrent', UCHAR),
    ('IFAIsFifo', UCHAR),
    ('IFAIsFifoTar', UCHAR),
    ('IFAIsFastSer', UCHAR),
    ('AIsVCP', UCHAR),
    ('IFBIsFifo', UCHAR),
    ('IFBIsFifoTar', UCHAR),
    ('IFBIsFastSer', UCHAR),
    ('BIsVCP', UCHAR),
    ('UseExtOsc', UCHAR),
    ('HighDriveIOs', UCHAR),
    ('EndpointSize', UCHAR),
    ('PullDownEnableR', UCHAR),
    ('SerNumEnableR', UCHAR),
    ('InvertTXD', UCHAR),
    ('InvertRXD', UCHAR),
    ('InvertRTS', UCHAR),
    ('InvertCTS', UCHAR),
    ('InvertDTR', UCHAR),
    ('InvertDSR', UCHAR),
    ('InvertDCD', UCHAR),
    ('InvertRI', UCHAR),
    ('Cbus0', UCHAR),
    ('Cbus1', UCHAR),
    ('Cbus2', UCHAR),
    ('Cbus3', UCHAR),
    ('Cbus4', UCHAR),
    ('RIsVCP', UCHAR),
]
PFT_PROGRAM_DATA = POINTER(ft_program_data)
FT_PROGRAM_DATA = ft_program_data
# ftd2xx.h 501
FT_EE_Program = _libraries['ftd2xx.dll'].FT_EE_Program
FT_EE_Program.restype = FT_STATUS
# FT_EE_Program(ftHandle, pData)
FT_EE_Program.argtypes = [FT_HANDLE, PFT_PROGRAM_DATA]
FT_EE_Program.__doc__ = \
"""FT_STATUS FT_EE_Program(FT_HANDLE ftHandle, PFT_PROGRAM_DATA pData)
ftd2xx.h:501"""
# ftd2xx.h 511
FT_EE_ProgramEx = _libraries['ftd2xx.dll'].FT_EE_ProgramEx
FT_EE_ProgramEx.restype = FT_STATUS
# FT_EE_ProgramEx(ftHandle, pData, Manufacturer, ManufacturerId, Description, SerialNumber)
FT_EE_ProgramEx.argtypes = [FT_HANDLE, PFT_PROGRAM_DATA, STRING, STRING, STRING, STRING]
FT_EE_ProgramEx.__doc__ = \
"""FT_STATUS FT_EE_ProgramEx(FT_HANDLE ftHandle, PFT_PROGRAM_DATA pData, char * Manufacturer, char * ManufacturerId, char * Description, char * SerialNumber)
ftd2xx.h:511"""
# ftd2xx.h 517
FT_EE_Read = _libraries['ftd2xx.dll'].FT_EE_Read
FT_EE_Read.restype = FT_STATUS
# FT_EE_Read(ftHandle, pData)
FT_EE_Read.argtypes = [FT_HANDLE, PFT_PROGRAM_DATA]
FT_EE_Read.__doc__ = \
"""FT_STATUS FT_EE_Read(FT_HANDLE ftHandle, PFT_PROGRAM_DATA pData)
ftd2xx.h:517"""
# ftd2xx.h 527
FT_EE_ReadEx = _libraries['ftd2xx.dll'].FT_EE_ReadEx
FT_EE_ReadEx.restype = FT_STATUS
# FT_EE_ReadEx(ftHandle, pData, Manufacturer, ManufacturerId, Description, SerialNumber)
FT_EE_ReadEx.argtypes = [FT_HANDLE, PFT_PROGRAM_DATA, STRING, STRING, STRING, STRING]
FT_EE_ReadEx.__doc__ = \
"""FT_STATUS FT_EE_ReadEx(FT_HANDLE ftHandle, PFT_PROGRAM_DATA pData, char * Manufacturer, char * ManufacturerId, char * Description, char * SerialNumber)
ftd2xx.h:527"""
# ftd2xx.h 533
FT_EE_UASize = _libraries['ftd2xx.dll'].FT_EE_UASize
FT_EE_UASize.restype = FT_STATUS
# FT_EE_UASize(ftHandle, lpdwSize)
FT_EE_UASize.argtypes = [FT_HANDLE, LPDWORD]
FT_EE_UASize.__doc__ = \
"""FT_STATUS FT_EE_UASize(FT_HANDLE ftHandle, LPDWORD lpdwSize)
ftd2xx.h:533"""
# ftd2xx.h 540
FT_EE_UAWrite = _libraries['ftd2xx.dll'].FT_EE_UAWrite
FT_EE_UAWrite.restype = FT_STATUS
# FT_EE_UAWrite(ftHandle, pucData, dwDataLen)
FT_EE_UAWrite.argtypes = [FT_HANDLE, PUCHAR, DWORD]
FT_EE_UAWrite.__doc__ = \
"""FT_STATUS FT_EE_UAWrite(FT_HANDLE ftHandle, PUCHAR pucData, DWORD dwDataLen)
ftd2xx.h:540"""
# ftd2xx.h 548
FT_EE_UARead = _libraries['ftd2xx.dll'].FT_EE_UARead
FT_EE_UARead.restype = FT_STATUS
# FT_EE_UARead(ftHandle, pucData, dwDataLen, lpdwBytesRead)
FT_EE_UARead.argtypes = [FT_HANDLE, PUCHAR, DWORD, LPDWORD]
FT_EE_UARead.__doc__ = \
"""FT_STATUS FT_EE_UARead(FT_HANDLE ftHandle, PUCHAR pucData, DWORD dwDataLen, LPDWORD lpdwBytesRead)
ftd2xx.h:548"""
# ftd2xx.h 554
FT_SetLatencyTimer = _libraries['ftd2xx.dll'].FT_SetLatencyTimer
FT_SetLatencyTimer.restype = FT_STATUS
# FT_SetLatencyTimer(ftHandle, ucLatency)
FT_SetLatencyTimer.argtypes = [FT_HANDLE, UCHAR]
FT_SetLatencyTimer.__doc__ = \
"""FT_STATUS FT_SetLatencyTimer(FT_HANDLE ftHandle, UCHAR ucLatency)
ftd2xx.h:554"""
# ftd2xx.h 560
FT_GetLatencyTimer = _libraries['ftd2xx.dll'].FT_GetLatencyTimer
FT_GetLatencyTimer.restype = FT_STATUS
# FT_GetLatencyTimer(ftHandle, pucLatency)
FT_GetLatencyTimer.argtypes = [FT_HANDLE, PUCHAR]
FT_GetLatencyTimer.__doc__ = \
"""FT_STATUS FT_GetLatencyTimer(FT_HANDLE ftHandle, PUCHAR pucLatency)
ftd2xx.h:560"""
# ftd2xx.h 567
FT_SetBitMode = _libraries['ftd2xx.dll'].FT_SetBitMode
FT_SetBitMode.restype = FT_STATUS
# FT_SetBitMode(ftHandle, ucMask, ucEnable)
FT_SetBitMode.argtypes = [FT_HANDLE, UCHAR, UCHAR]
FT_SetBitMode.__doc__ = \
"""FT_STATUS FT_SetBitMode(FT_HANDLE ftHandle, UCHAR ucMask, UCHAR ucEnable)
ftd2xx.h:567"""
# ftd2xx.h 573
FT_GetBitMode = _libraries['ftd2xx.dll'].FT_GetBitMode
FT_GetBitMode.restype = FT_STATUS
# FT_GetBitMode(ftHandle, pucMode)
FT_GetBitMode.argtypes = [FT_HANDLE, PUCHAR]
FT_GetBitMode.__doc__ = \
"""FT_STATUS FT_GetBitMode(FT_HANDLE ftHandle, PUCHAR pucMode)
ftd2xx.h:573"""
# ftd2xx.h 580
FT_SetUSBParameters = _libraries['ftd2xx.dll'].FT_SetUSBParameters
FT_SetUSBParameters.restype = FT_STATUS
# FT_SetUSBParameters(ftHandle, ulInTransferSize, ulOutTransferSize)
FT_SetUSBParameters.argtypes = [FT_HANDLE, ULONG, ULONG]
FT_SetUSBParameters.__doc__ = \
"""FT_STATUS FT_SetUSBParameters(FT_HANDLE ftHandle, ULONG ulInTransferSize, ULONG ulOutTransferSize)
ftd2xx.h:580"""
# ftd2xx.h 586
FT_SetDeadmanTimeout = _libraries['ftd2xx.dll'].FT_SetDeadmanTimeout
FT_SetDeadmanTimeout.restype = FT_STATUS
# FT_SetDeadmanTimeout(ftHandle, ulDeadmanTimeout)
FT_SetDeadmanTimeout.argtypes = [FT_HANDLE, ULONG]
FT_SetDeadmanTimeout.__doc__ = \
"""FT_STATUS FT_SetDeadmanTimeout(FT_HANDLE ftHandle, ULONG ulDeadmanTimeout)
ftd2xx.h:586"""
# ftd2xx.h 596
FT_GetDeviceInfo = _libraries['ftd2xx.dll'].FT_GetDeviceInfo
FT_GetDeviceInfo.restype = FT_STATUS
# FT_GetDeviceInfo(ftHandle, lpftDevice, lpdwID, SerialNumber, Description, Dummy)
FT_GetDeviceInfo.argtypes = [FT_HANDLE, POINTER(FT_DEVICE), LPDWORD, PCHAR, PCHAR, LPVOID]
FT_GetDeviceInfo.__doc__ = \
"""FT_STATUS FT_GetDeviceInfo(FT_HANDLE ftHandle, FT_DEVICE * lpftDevice, LPDWORD lpdwID, PCHAR SerialNumber, PCHAR Description, LPVOID Dummy)
ftd2xx.h:596"""
# ftd2xx.h 601
FT_StopInTask = _libraries['ftd2xx.dll'].FT_StopInTask
FT_StopInTask.restype = FT_STATUS
# FT_StopInTask(ftHandle)
FT_StopInTask.argtypes = [FT_HANDLE]
FT_StopInTask.__doc__ = \
"""FT_STATUS FT_StopInTask(FT_HANDLE ftHandle)
ftd2xx.h:601"""
# ftd2xx.h 606
FT_RestartInTask = _libraries['ftd2xx.dll'].FT_RestartInTask
FT_RestartInTask.restype = FT_STATUS
# FT_RestartInTask(ftHandle)
FT_RestartInTask.argtypes = [FT_HANDLE]
FT_RestartInTask.__doc__ = \
"""FT_STATUS FT_RestartInTask(FT_HANDLE ftHandle)
ftd2xx.h:606"""
# ftd2xx.h 612
FT_SetResetPipeRetryCount = _libraries['ftd2xx.dll'].FT_SetResetPipeRetryCount
FT_SetResetPipeRetryCount.restype = FT_STATUS
# FT_SetResetPipeRetryCount(ftHandle, dwCount)
FT_SetResetPipeRetryCount.argtypes = [FT_HANDLE, DWORD]
FT_SetResetPipeRetryCount.__doc__ = \
"""FT_STATUS FT_SetResetPipeRetryCount(FT_HANDLE ftHandle, DWORD dwCount)
ftd2xx.h:612"""
# ftd2xx.h 617
FT_ResetPort = _libraries['ftd2xx.dll'].FT_ResetPort
FT_ResetPort.restype = FT_STATUS
# FT_ResetPort(ftHandle)
FT_ResetPort.argtypes = [FT_HANDLE]
FT_ResetPort.__doc__ = \
"""FT_STATUS FT_ResetPort(FT_HANDLE ftHandle)
ftd2xx.h:617"""
# ftd2xx.h 622
FT_CyclePort = _libraries['ftd2xx.dll'].FT_CyclePort
FT_CyclePort.restype = FT_STATUS
# FT_CyclePort(ftHandle)
FT_CyclePort.argtypes = [FT_HANDLE]
FT_CyclePort.__doc__ = \
"""FT_STATUS FT_CyclePort(FT_HANDLE ftHandle)
ftd2xx.h:622"""
# ftd2xx.h 638
FT_W32_CreateFile = _libraries['ftd2xx.dll'].FT_W32_CreateFile
FT_W32_CreateFile.restype = FT_HANDLE
# FT_W32_CreateFile(lpszName, dwAccess, dwShareMode, lpSecurityAttributes, dwCreate, dwAttrsAndFlags, hTemplate)
FT_W32_CreateFile.argtypes = [LPCSTR, DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD, DWORD, HANDLE]
FT_W32_CreateFile.__doc__ = \
"""FT_HANDLE FT_W32_CreateFile(LPCSTR lpszName, DWORD dwAccess, DWORD dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, DWORD dwCreate, DWORD dwAttrsAndFlags, HANDLE hTemplate)
ftd2xx.h:638"""
# ftd2xx.h 643
FT_W32_CloseHandle = _libraries['ftd2xx.dll'].FT_W32_CloseHandle
FT_W32_CloseHandle.restype = BOOL
# FT_W32_CloseHandle(ftHandle)
FT_W32_CloseHandle.argtypes = [FT_HANDLE]
FT_W32_CloseHandle.__doc__ = \
"""BOOL FT_W32_CloseHandle(FT_HANDLE ftHandle)
ftd2xx.h:643"""
# ftd2xx.h 652
FT_W32_ReadFile = _libraries['ftd2xx.dll'].FT_W32_ReadFile
FT_W32_ReadFile.restype = BOOL
# FT_W32_ReadFile(ftHandle, lpBuffer, nBufferSize, lpBytesReturned, lpOverlapped)
FT_W32_ReadFile.argtypes = [FT_HANDLE, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
FT_W32_ReadFile.__doc__ = \
"""BOOL FT_W32_ReadFile(FT_HANDLE ftHandle, LPVOID lpBuffer, DWORD nBufferSize, LPDWORD lpBytesReturned, LPOVERLAPPED lpOverlapped)
ftd2xx.h:652"""
# ftd2xx.h 661
FT_W32_WriteFile = _libraries['ftd2xx.dll'].FT_W32_WriteFile
FT_W32_WriteFile.restype = BOOL
# FT_W32_WriteFile(ftHandle, lpBuffer, nBufferSize, lpBytesWritten, lpOverlapped)
FT_W32_WriteFile.argtypes = [FT_HANDLE, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
FT_W32_WriteFile.__doc__ = \
"""BOOL FT_W32_WriteFile(FT_HANDLE ftHandle, LPVOID lpBuffer, DWORD nBufferSize, LPDWORD lpBytesWritten, LPOVERLAPPED lpOverlapped)
ftd2xx.h:661"""
# ftd2xx.h 666
FT_W32_GetLastError = _libraries['ftd2xx.dll'].FT_W32_GetLastError
FT_W32_GetLastError.restype = DWORD
# FT_W32_GetLastError(ftHandle)
FT_W32_GetLastError.argtypes = [FT_HANDLE]
FT_W32_GetLastError.__doc__ = \
"""DWORD FT_W32_GetLastError(FT_HANDLE ftHandle)
ftd2xx.h:666"""
# ftd2xx.h 674
FT_W32_GetOverlappedResult = _libraries['ftd2xx.dll'].FT_W32_GetOverlappedResult
FT_W32_GetOverlappedResult.restype = BOOL
# FT_W32_GetOverlappedResult(ftHandle, lpOverlapped, lpdwBytesTransferred, bWait)
FT_W32_GetOverlappedResult.argtypes = [FT_HANDLE, LPOVERLAPPED, LPDWORD, BOOL]
FT_W32_GetOverlappedResult.__doc__ = \
"""BOOL FT_W32_GetOverlappedResult(FT_HANDLE ftHandle, LPOVERLAPPED lpOverlapped, LPDWORD lpdwBytesTransferred, BOOL bWait)
ftd2xx.h:674"""
# ftd2xx.h 679
FT_W32_CancelIo = _libraries['ftd2xx.dll'].FT_W32_CancelIo
FT_W32_CancelIo.restype = BOOL
# FT_W32_CancelIo(ftHandle)
FT_W32_CancelIo.argtypes = [FT_HANDLE]
FT_W32_CancelIo.__doc__ = \
"""BOOL FT_W32_CancelIo(FT_HANDLE ftHandle)
ftd2xx.h:679"""
# ftd2xx.h 685
class _FTCOMSTAT(Structure):
    pass
_FTCOMSTAT._fields_ = [
    # ftd2xx.h 685
    ('fCtsHold', DWORD, 1),
    ('fDsrHold', DWORD, 1),
    ('fRlsdHold', DWORD, 1),
    ('fXoffHold', DWORD, 1),
    ('fXoffSent', DWORD, 1),
    ('fEof', DWORD, 1),
    ('fTxim', DWORD, 1),
    ('fReserved', DWORD, 25),
    ('cbInQue', DWORD),
    ('cbOutQue', DWORD),
]
LPFTCOMSTAT = POINTER(_FTCOMSTAT)
FTCOMSTAT = _FTCOMSTAT
# ftd2xx.h 698
class _FTDCB(Structure):
    pass
_FTDCB._fields_ = [
    # ftd2xx.h 698
    ('DCBlength', DWORD),
    ('BaudRate', DWORD),
    ('fBinary', DWORD, 1),
    ('fParity', DWORD, 1),
    ('fOutxCtsFlow', DWORD, 1),
    ('fOutxDsrFlow', DWORD, 1),
    ('fDtrControl', DWORD, 2),
    ('fDsrSensitivity', DWORD, 1),
    ('fTXContinueOnXoff', DWORD, 1),
    ('fOutX', DWORD, 1),
    ('fInX', DWORD, 1),
    ('fErrorChar', DWORD, 1),
    ('fNull', DWORD, 1),
    ('fRtsControl', DWORD, 2),
    ('fAbortOnError', DWORD, 1),
    ('fDummy2', DWORD, 17),
    ('wReserved', WORD),
    ('XonLim', WORD),
    ('XoffLim', WORD),
    ('ByteSize', BYTE),
    ('Parity', BYTE),
    ('StopBits', BYTE),
    ('XonChar', c_char),
    ('XoffChar', c_char),
    ('ErrorChar', c_char),
    ('EofChar', c_char),
    ('EvtChar', c_char),
    ('wReserved1', WORD),
]
FTDCB = _FTDCB
LPFTDCB = POINTER(_FTDCB)
# ftd2xx.h 729
class _FTTIMEOUTS(Structure):
    pass
_FTTIMEOUTS._fields_ = [
    # ftd2xx.h 729
    ('ReadIntervalTimeout', DWORD),
    ('ReadTotalTimeoutMultiplier', DWORD),
    ('ReadTotalTimeoutConstant', DWORD),
    ('WriteTotalTimeoutMultiplier', DWORD),
    ('WriteTotalTimeoutConstant', DWORD),
]
FTTIMEOUTS = _FTTIMEOUTS
LPFTTIMEOUTS = POINTER(_FTTIMEOUTS)
# ftd2xx.h 741
FT_W32_ClearCommBreak = _libraries['ftd2xx.dll'].FT_W32_ClearCommBreak
FT_W32_ClearCommBreak.restype = BOOL
# FT_W32_ClearCommBreak(ftHandle)
FT_W32_ClearCommBreak.argtypes = [FT_HANDLE]
FT_W32_ClearCommBreak.__doc__ = \
"""BOOL FT_W32_ClearCommBreak(FT_HANDLE ftHandle)
ftd2xx.h:741"""
# ftd2xx.h 748
FT_W32_ClearCommError = _libraries['ftd2xx.dll'].FT_W32_ClearCommError
FT_W32_ClearCommError.restype = BOOL
# FT_W32_ClearCommError(ftHandle, lpdwErrors, lpftComstat)
FT_W32_ClearCommError.argtypes = [FT_HANDLE, LPDWORD, LPFTCOMSTAT]
FT_W32_ClearCommError.__doc__ = \
"""BOOL FT_W32_ClearCommError(FT_HANDLE ftHandle, LPDWORD lpdwErrors, LPFTCOMSTAT lpftComstat)
ftd2xx.h:748"""
# ftd2xx.h 754
FT_W32_EscapeCommFunction = _libraries['ftd2xx.dll'].FT_W32_EscapeCommFunction
FT_W32_EscapeCommFunction.restype = BOOL
# FT_W32_EscapeCommFunction(ftHandle, dwFunc)
FT_W32_EscapeCommFunction.argtypes = [FT_HANDLE, DWORD]
FT_W32_EscapeCommFunction.__doc__ = \
"""BOOL FT_W32_EscapeCommFunction(FT_HANDLE ftHandle, DWORD dwFunc)
ftd2xx.h:754"""
# ftd2xx.h 760
FT_W32_GetCommModemStatus = _libraries['ftd2xx.dll'].FT_W32_GetCommModemStatus
FT_W32_GetCommModemStatus.restype = BOOL
# FT_W32_GetCommModemStatus(ftHandle, lpdwModemStatus)
FT_W32_GetCommModemStatus.argtypes = [FT_HANDLE, LPDWORD]
FT_W32_GetCommModemStatus.__doc__ = \
"""BOOL FT_W32_GetCommModemStatus(FT_HANDLE ftHandle, LPDWORD lpdwModemStatus)
ftd2xx.h:760"""
# ftd2xx.h 766
FT_W32_GetCommState = _libraries['ftd2xx.dll'].FT_W32_GetCommState
FT_W32_GetCommState.restype = BOOL
# FT_W32_GetCommState(ftHandle, lpftDcb)
FT_W32_GetCommState.argtypes = [FT_HANDLE, LPFTDCB]
FT_W32_GetCommState.__doc__ = \
"""BOOL FT_W32_GetCommState(FT_HANDLE ftHandle, LPFTDCB lpftDcb)
ftd2xx.h:766"""
# ftd2xx.h 772
FT_W32_GetCommTimeouts = _libraries['ftd2xx.dll'].FT_W32_GetCommTimeouts
FT_W32_GetCommTimeouts.restype = BOOL
# FT_W32_GetCommTimeouts(ftHandle, pTimeouts)
FT_W32_GetCommTimeouts.argtypes = [FT_HANDLE, POINTER(FTTIMEOUTS)]
FT_W32_GetCommTimeouts.__doc__ = \
"""BOOL FT_W32_GetCommTimeouts(FT_HANDLE ftHandle, FTTIMEOUTS * pTimeouts)
ftd2xx.h:772"""
# ftd2xx.h 778
FT_W32_PurgeComm = _libraries['ftd2xx.dll'].FT_W32_PurgeComm
FT_W32_PurgeComm.restype = BOOL
# FT_W32_PurgeComm(ftHandle, dwMask)
FT_W32_PurgeComm.argtypes = [FT_HANDLE, DWORD]
FT_W32_PurgeComm.__doc__ = \
"""BOOL FT_W32_PurgeComm(FT_HANDLE ftHandle, DWORD dwMask)
ftd2xx.h:778"""
# ftd2xx.h 783
FT_W32_SetCommBreak = _libraries['ftd2xx.dll'].FT_W32_SetCommBreak
FT_W32_SetCommBreak.restype = BOOL
# FT_W32_SetCommBreak(ftHandle)
FT_W32_SetCommBreak.argtypes = [FT_HANDLE]
FT_W32_SetCommBreak.__doc__ = \
"""BOOL FT_W32_SetCommBreak(FT_HANDLE ftHandle)
ftd2xx.h:783"""
# ftd2xx.h 789
FT_W32_SetCommMask = _libraries['ftd2xx.dll'].FT_W32_SetCommMask
FT_W32_SetCommMask.restype = BOOL
# FT_W32_SetCommMask(ftHandle, ulEventMask)
FT_W32_SetCommMask.argtypes = [FT_HANDLE, ULONG]
FT_W32_SetCommMask.__doc__ = \
"""BOOL FT_W32_SetCommMask(FT_HANDLE ftHandle, ULONG ulEventMask)
ftd2xx.h:789"""
# ftd2xx.h 795
FT_W32_SetCommState = _libraries['ftd2xx.dll'].FT_W32_SetCommState
FT_W32_SetCommState.restype = BOOL
# FT_W32_SetCommState(ftHandle, lpftDcb)
FT_W32_SetCommState.argtypes = [FT_HANDLE, LPFTDCB]
FT_W32_SetCommState.__doc__ = \
"""BOOL FT_W32_SetCommState(FT_HANDLE ftHandle, LPFTDCB lpftDcb)
ftd2xx.h:795"""
# ftd2xx.h 801
FT_W32_SetCommTimeouts = _libraries['ftd2xx.dll'].FT_W32_SetCommTimeouts
FT_W32_SetCommTimeouts.restype = BOOL
# FT_W32_SetCommTimeouts(ftHandle, pTimeouts)
FT_W32_SetCommTimeouts.argtypes = [FT_HANDLE, POINTER(FTTIMEOUTS)]
FT_W32_SetCommTimeouts.__doc__ = \
"""BOOL FT_W32_SetCommTimeouts(FT_HANDLE ftHandle, FTTIMEOUTS * pTimeouts)
ftd2xx.h:801"""
# ftd2xx.h 808
FT_W32_SetupComm = _libraries['ftd2xx.dll'].FT_W32_SetupComm
FT_W32_SetupComm.restype = BOOL
# FT_W32_SetupComm(ftHandle, dwReadBufferSize, dwWriteBufferSize)
FT_W32_SetupComm.argtypes = [FT_HANDLE, DWORD, DWORD]
FT_W32_SetupComm.__doc__ = \
"""BOOL FT_W32_SetupComm(FT_HANDLE ftHandle, DWORD dwReadBufferSize, DWORD dwWriteBufferSize)
ftd2xx.h:808"""
# ftd2xx.h 815
FT_W32_WaitCommEvent = _libraries['ftd2xx.dll'].FT_W32_WaitCommEvent
FT_W32_WaitCommEvent.restype = BOOL
# FT_W32_WaitCommEvent(ftHandle, pulEvent, lpOverlapped)
FT_W32_WaitCommEvent.argtypes = [FT_HANDLE, PULONG, LPOVERLAPPED]
FT_W32_WaitCommEvent.__doc__ = \
"""BOOL FT_W32_WaitCommEvent(FT_HANDLE ftHandle, PULONG pulEvent, LPOVERLAPPED lpOverlapped)
ftd2xx.h:815"""
# ftd2xx.h 822
class _ft_device_list_info_node(Structure):
    pass
_ft_device_list_info_node._fields_ = [
    # ftd2xx.h 822
    ('Flags', ULONG),
    ('Type', ULONG),
    ('ID', ULONG),
    ('LocId', DWORD),
    ('SerialNumber', c_char * 16),
    ('Description', c_char * 64),
    ('ftHandle', FT_HANDLE),
]
FT_DEVICE_LIST_INFO_NODE = _ft_device_list_info_node
# ftd2xx.h 836
FT_CreateDeviceInfoList = _libraries['ftd2xx.dll'].FT_CreateDeviceInfoList
FT_CreateDeviceInfoList.restype = FT_STATUS
# FT_CreateDeviceInfoList(lpdwNumDevs)
FT_CreateDeviceInfoList.argtypes = [LPDWORD]
FT_CreateDeviceInfoList.__doc__ = \
"""FT_STATUS FT_CreateDeviceInfoList(LPDWORD lpdwNumDevs)
ftd2xx.h:836"""
# ftd2xx.h 842
FT_GetDeviceInfoList = _libraries['ftd2xx.dll'].FT_GetDeviceInfoList
FT_GetDeviceInfoList.restype = FT_STATUS
# FT_GetDeviceInfoList(pDest, lpdwNumDevs)
FT_GetDeviceInfoList.argtypes = [POINTER(FT_DEVICE_LIST_INFO_NODE), LPDWORD]
FT_GetDeviceInfoList.__doc__ = \
"""FT_STATUS FT_GetDeviceInfoList(FT_DEVICE_LIST_INFO_NODE * pDest, LPDWORD lpdwNumDevs)
ftd2xx.h:842"""
# ftd2xx.h 854
FT_GetDeviceInfoDetail = _libraries['ftd2xx.dll'].FT_GetDeviceInfoDetail
FT_GetDeviceInfoDetail.restype = FT_STATUS
# FT_GetDeviceInfoDetail(dwIndex, lpdwFlags, lpdwType, lpdwID, lpdwLocId, lpSerialNumber, lpDescription, pftHandle)
FT_GetDeviceInfoDetail.argtypes = [DWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPVOID, LPVOID, POINTER(FT_HANDLE)]
FT_GetDeviceInfoDetail.__doc__ = \
"""FT_STATUS FT_GetDeviceInfoDetail(DWORD dwIndex, LPDWORD lpdwFlags, LPDWORD lpdwType, LPDWORD lpdwID, LPDWORD lpdwLocId, LPVOID lpSerialNumber, LPVOID lpDescription, FT_HANDLE * pftHandle)
ftd2xx.h:854"""
# ftd2xx.h 865
FT_GetDriverVersion = _libraries['ftd2xx.dll'].FT_GetDriverVersion
FT_GetDriverVersion.restype = FT_STATUS
# FT_GetDriverVersion(ftHandle, lpdwVersion)
FT_GetDriverVersion.argtypes = [FT_HANDLE, LPDWORD]
FT_GetDriverVersion.__doc__ = \
"""FT_STATUS FT_GetDriverVersion(FT_HANDLE ftHandle, LPDWORD lpdwVersion)
ftd2xx.h:865"""
# ftd2xx.h 870
FT_GetLibraryVersion = _libraries['ftd2xx.dll'].FT_GetLibraryVersion
FT_GetLibraryVersion.restype = FT_STATUS
# FT_GetLibraryVersion(lpdwVersion)
FT_GetLibraryVersion.argtypes = [LPDWORD]
FT_GetLibraryVersion.__doc__ = \
"""FT_STATUS FT_GetLibraryVersion(LPDWORD lpdwVersion)
ftd2xx.h:870"""
# ftd2xx.h 899
FT_GetComPortNumber = _libraries['ftd2xx.dll'].FT_GetComPortNumber
FT_GetComPortNumber.restype = FT_STATUS
# FT_GetComPortNumber(ftHandle, lpdwComPortNumber)
FT_GetComPortNumber.argtypes = [FT_HANDLE, LPLONG]
FT_GetComPortNumber.__doc__ = \
"""FT_STATUS FT_GetComPortNumber(FT_HANDLE ftHandle, LPLONG lpdwComPortNumber)
ftd2xx.h:899"""
__all__ = ['FT_DEVICE_232R', 'FT_STATUS', 'FT_GetLibraryVersion',
           'VOID', 'FT_GetLatencyTimer', 'FT_EE_ProgramEx',
           'FT_SetEventNotification', 'FT_GetDeviceInfoList',
           'FT_OpenEx', 'FT_INVALID_ARGS', 'FT_W32_WriteFile',
           'FT_StopInTask', '_FTCOMSTAT', 'FT_GetDeviceInfo',
           'FT_DEVICE_100AX', 'FT_W32_SetCommTimeouts',
           'PFT_PROGRAM_DATA', 'FT_W32_WaitCommEvent', 'PUCHAR',
           'FT_W32_ReadFile', 'FT_ResetDevice', 'FT_ResetPort',
           'FT_GetStatus', 'FT_SetDataCharacteristics', 'FT_ClrRts',
           'FT_W32_CancelIo', 'FT_EEPROM_WRITE_FAILED', 'FT_Close',
           'FT_GetModemStatus', 'FT_W32_CreateFile', 'LPFTTIMEOUTS',
           'FT_Write', 'FT_W32_GetCommModemStatus', 'FT_SetBreakOff',
           '_FTTIMEOUTS', 'LPVOID', 'FT_DEVICE_BM', 'FT_SetBreakOn',
           'FT_W32_GetCommState', 'FT_SetBaudRate',
           'FT_SetResetPipeRetryCount', 'FTTIMEOUTS',
           'FT_INVALID_PARAMETER', 'SHORT',
           'FT_FAILED_TO_WRITE_DEVICE', 'FT_NOT_SUPPORTED',
           'FT_ReadEE', 'FT_Open', 'FT_DEVICE_2232C',
           'FT_W32_GetCommTimeouts', 'FT_CreateDeviceInfoList',
           'FT_SetRts', 'LPSECURITY_ATTRIBUTES', 'FT_DEVICE_AM',
           'FT_SetBitMode', 'FT_DEVICE_NOT_OPENED_FOR_ERASE',
           'FT_EE_Program', 'FT_W32_GetLastError', 'UCHAR', 'LPFTDCB',
           'FT_DEVICE_NOT_FOUND', 'FT_W32_GetOverlappedResult',
           'OVERLAPPED', 'INT', 'FT_SetDivisor', 'LPFTCOMSTAT',
           'FT_W32_SetCommBreak', 'FT_DEVICE_NOT_OPENED_FOR_WRITE',
           'PULONG', 'FT_EEPROM_NOT_PROGRAMMED', 'FT_ClrDtr',
           'SYSTEMTIME', 'FT_SetDtr', 'LPWORD', 'FT_SetUSBParameters',
           'FT_Read', 'CHAR', 'FT_DEVICE_NOT_OPENED', 'LPBYTE',
           'FT_ListDevices', 'PFT_EVENT_HANDLER', 'FT_EE_UARead',
           'FT_W32_SetupComm', 'FT_WriteEE',
           'FT_INSUFFICIENT_RESOURCES', 'FT_EE_ReadEx',
           'SECURITY_ATTRIBUTES', 'FT_W32_PurgeComm', 'FT_CyclePort',
           'FT_SetDeadmanTimeout', 'FTDCB',
           'FT_DEVICE_LIST_INFO_NODE', 'FT_GetEventStatus',
           'FT_W32_CloseHandle', 'FT_EE_Read', 'FT_PROGRAM_DATA',
           '_ft_device_list_info_node', 'FT_EEPROM_NOT_PRESENT',
           '_FTDCB', 'FT_EEPROM_READ_FAILED', 'FT_HANDLE', 'USHORT',
           'LPDWORD', 'FT_GetBitMode', 'FT_IoCtl', 'FT_SetChars',
           'FT_RestartInTask', 'FT_SetLatencyTimer', 'LPTSTR',
           'FT_Purge', 'FT_EE_UAWrite', 'LPBOOL',
           '_SECURITY_ATTRIBUTES', 'FT_IO_ERROR',
           'FT_W32_ClearCommBreak', 'FT_GetDriverVersion', 'timeval',
           'LPOVERLAPPED', 'FT_GetDeviceInfoDetail',
           'FT_SetFlowControl', 'FT_INVALID_HANDLE',
           'FT_EEPROM_ERASE_FAILED', 'FT_W32_EscapeCommFunction',
           'PCHAR', 'FT_GetQueueStatus', 'ULONGLONG', 'FT_OK',
           'FTCOMSTAT', 'FT_WaitOnMask', 'FT_SetTimeouts',
           '_OVERLAPPED', 'FT_W32_ClearCommError', 'FT_EraseEE',
           'FT_W32_SetCommState', 'FT_INVALID_BAUD_RATE',
           'FT_SetWaitMask', 'FT_EE_UASize', 'FT_DEVICE_UNKNOWN',
           'FT_DEVICE', 'FT_OTHER_ERROR', 'ft_program_data', 'PVOID',
           'FT_W32_SetCommMask', 'LPLONG', 'FT_GetComPortNumber']