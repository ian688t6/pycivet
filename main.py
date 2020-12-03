import logging
import argparse
import os
import sys
from prx import Prx

def log_show(prx):
    try:
        prx.getlog()
    except BaseException as e:
        if isinstance(e, KeyboardInterrupt):
            print('pycivet exit')
            prx.disconnect()
            sys.exit(0)

def log_save(prx, logfile):
    print(logfile)
    logging.basicConfig(filename=logfile, encoding='utf-8', format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    log_show(prx)

if __name__ == "__main__":
    # Todo: initial logging module
    print('welcome using pycivet')
    
    parser = argparse.ArgumentParser(description='pycivet')
    parser.add_argument('--log', nargs="?", type=str, default=None, const='', help='show rx running log')
    args = parser.parse_args()
    if len(args._get_args()) == 0:
        sys.exit(0)
    rx = Prx()
    rx.connect()
    if args.log != None:
        if args.log == "":
            logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
            log_show(rx)
        else:
            log_save(rx, args.log)
        pass
    rx.disconnect()
    print('pycivet quit')
