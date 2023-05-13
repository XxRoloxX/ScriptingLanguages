import eel
import threading
from subprocess import call
from time import sleep
from SSHLogJournal import SSHLogJournal
from logUtils import openFile


mainJournal = [SSHLogJournal()]


SSHJokes = [
    "I love reading SSH logs. It's like a thriller novel where the villain is always \"root\".",
    "I'm not saying I'm addicted to reading SSH logs, but I can't help checking them every time I pass by a computer.",
    "Why did the sysadmin cross the road? To get to the other side of the SSH connection.",
    "I read through my SSH logs for hours last night. It was boring, but I couldn't stop. I think I have terminal illness.",
    "I tried to tell a joke about SSH logs, but I got \"Permission denied\".",
    "Why did the chicken log into the server? To check its SSH log.",
    "Why did the sysadmin go to the beach? To catch some SSH.",
    "You know you're a sysadmin when you laugh at jokes about SSH logs.",
    "SSH logs are like a box of chocolates, you never know what you're going to get - except for a lot of failed login attempts.",
    "Reading SSH logs is like a treasure hunt, but instead of gold, you find lots of attempts to brute force your password."
]

@eel.expose
def getJoke(jokeIndex):
    jokeIndex%=len(SSHJokes)
    print(SSHJokes[jokeIndex])
    return SSHJokes[jokeIndex]


@eel.expose
def getLogJournalFromFile(filepath):
    print("Python function is run")
    mainJournal[0] = SSHLogJournal()
    openFile(filepath,[mainJournal[0].append])
    return mainJournal[0].getListOfRawLogs()
    #return ["a","b"]


@eel.expose
def filterJournalByDates(startDate, endDate):
    print("Filter  is run")
    #startDate="2023-12-10"
    #endDate = "2023-12-10"
    newJournal =  mainJournal[0].filterSSHLogJournalAfterDate(startDate, endDate).getListOfRawLogs()
    return newJournal



@eel.expose
def getLogDetails(logIndex):

    logEntry = mainJournal[0].get(logIndex)

    if not logEntry:
        return None

   

    result = {
        "user":logEntry.user,
        "ip":  logEntry.ip,
        "date": logEntry.stringifiedDate,
        "pid": logEntry.pid
    }

    print(result)
    
    return result


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
   