import logging
import argparse
import os
import sys
from cfs.prx import Prx

def log_show(prx):
    try:
        prx.get_log()
    except BaseException as e:
        if isinstance(e, KeyboardInterrupt):
            print('pycivet exit')
            prx.disconnect()
            sys.exit(0)

def log_save(prx, logfile):
    print(logfile)
    logging.basicConfig(filename=logfile, encoding='utf-8', format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    log_show(prx)

def firmware_download(prx, binfile):
    print(binfile)
    prx.writesram(0x50100088, 0x01)
    prx.writesram(0x50100031, 0x00)
    prx.writesram(0x50100038, 0xFF)
    prx.writesram(0x38000074, 0x10)
    prx.writesram(0x38000075, 0x10)
    prx.writesram(0x50020000, 0x00)
    prx.writesram(0x50020040, 0x00)
    prx.writesram(0x3800005F, 0x44)

    if prx.download(binfile, 1) == True:
        print("Download Success")
    else:
        print("Download Failure")
    prx.writesram(0x50100031, 0x01)

if __name__ == "__main__":
    # Todo: initial logging module
    print('welcome using pycivet')
    
    parser = argparse.ArgumentParser(description='pycivet host tool for debug and download firmware')
    parser.add_argument('--log', metavar='xxxx.txt', nargs="?", type=str, default=None, const='', help='show rx running log')
    parser.add_argument('--download', metavar='xxxx.bin', nargs=1, type=str, help='download the firmware')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    rx = Prx()
    # rx.connect(b'UM232H')
    rx.connect(b'FT4222 A')
    if args.log != None:
        if args.log == "":
            logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
            log_show(rx)
        else:
            log_save(rx, args.log)
        
    if len(args.download) > 0:
        firmware_download(rx, args.download[0])

    rx.disconnect()
    print('pycivet quit')
