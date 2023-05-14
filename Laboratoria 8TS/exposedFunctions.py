import eel
from newLogTools.SSHLogJournal import SSHLogJournal
from newLogTools.Zadanie1 import *

mainJournal = [SSHLogJournal()]
filteredJournal = [SSHLogJournal()]

INITIAL_LOGS_RETRIEVED = 15
DEFAULT_LOG_LENGTH =100


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
    print(filepath+" is being read")
    mainJournal[0] = SSHLogJournal()
    openFile(filepath,[mainJournal[0].append])
    filteredJournal[0]=mainJournal[0]

    if len(mainJournal[0])==0:
        return None
    else:
        return filteredJournal[0].getListOfRawLogs(DEFAULT_LOG_LENGTH)[0:INITIAL_LOGS_RETRIEVED]
    

@eel.expose
def getNLogsFromFile(startIndex, numberOfLogsToRetrieve):
    return filteredJournal[0].getListOfRawLogs(DEFAULT_LOG_LENGTH)[startIndex:startIndex+numberOfLogsToRetrieve:1]



@eel.expose
def filterJournalByDates(startDate, endDate):
    print("Filter  is run")
    filteredJournal[0]=mainJournal[0].filterSSHLogJournalAfterDate(startDate, endDate)
    return filteredJournal[0].getListOfRawLogs(DEFAULT_LOG_LENGTH)[0:INITIAL_LOGS_RETRIEVED]



@eel.expose
def getLogDetails(logIndex):

    logEntry = filteredJournal[0].get(logIndex)

    if not logEntry:
        return None

    result = {
        "user":logEntry.user,
        "ip":  logEntry.ip,
        "date": logEntry.stringifiedDate,
        "pid": logEntry.pid,
        "type": logEntry.log_type
    }
    if isinstance(logEntry, SSHLogLogin):
        result["port"] = logEntry.userPort

    print(result)
    
    return result


@eel.expose
def printHello(x):
    print(x)
    return x