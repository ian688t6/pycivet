from prx import Prx

if __name__ == "__main__":
    print('welcome using pycivet')
    rx = Prx()
    rx.connect()
    rx.download()
    rx.disconnect()