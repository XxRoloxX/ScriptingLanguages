import eel
import threading
from subprocess import call
from time import sleep
from exposedFunctions import *

FRONT_PORT = 3000
EEL_PORT = 8888


def start_web():
    call(['./start.sh'])


def start_eel():
    sleep(3)
    eel.init('client')
    eel.start({"port": FRONT_PORT}, host="localhost", port=EEL_PORT)
    

if __name__ == '__main__':
    t1 = threading.Thread(target=start_web)
    t2 = threading.Thread(target=start_eel)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
   