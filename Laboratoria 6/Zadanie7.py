from Zadanie1 import *
from SSHLogJournal import *
from SSHUser import *
from logUtils import *
from parsingUtils import *


if __name__=="__main__":
    journal = SSHLogJournal()
    openFile("SSH/SSH.log",[journal.append])
    #sortedLogs = journal.getSortedCollection()
    filtered = journal[0:10:2][":46"]

    for logObj in filtered:
        print(logObj)

