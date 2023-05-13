import eel
import threading
from subprocess import call
from time import sleep
from SSHLogJournal import SSHLogJournal
from logUtils import openFile


mainJournal = SSHLogJournal()


@eel.expose
def getLogJournalFromFile(filepath):
    print("Python function is run")
    mainJournal = SSHLogJournal()
    openFile(filepath,[mainJournal.append])
    return mainJournal.getListOfRawLogs()
    #return ["a","b"]


@eel.expose
def filterJournalByDates(startDate, endDate):
    print("Filter  is run")
    newJournal =  mainJournal.filterSSHLogJournalAfterDate(startDate, endDate).getListOfRawLogs()
    for i in newJournal:
        print(i)






@eel.expose
def printHello(x):
    print(x)
    return x

def start_web():
    call(['./start.sh'])


def start_eel():
    sleep(3)
    eel.init('client')
    eel.start({"port": 3000}, host="localhost", port=8888)
    

if __name__ == '__main__':
    t1 = threading.Thread(target=start_web)
    t2 = threading.Thread(target=start_eel)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
   