import logging
import os
import sys
from prx import Prx

if __name__ == "__main__":
    # Todo: initial logging module
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info('welcome using pycivet')

    rx = Prx()
    rx.connect()
    # rx.download()

    try:
        rx.getlog()
    except BaseException as e:
        if isinstance(e, KeyboardInterrupt):
            logging.info('pycivet exit')
            rx.disconnect()
            sys.exit(0)
    rx.disconnect()

