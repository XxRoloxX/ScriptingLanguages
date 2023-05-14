from Zadanie1 import *
from SSHLogJournal import *
from SSHUser import *
from logUtils import *
from parsingUtils import *

if __name__=="__main__":
    journal = SSHLogJournal()
    openFile("SSH/SSH.log",[journal.append])
    users = []

    for entry in journal[0:500]:
        if isinstance(entry,SSHLogLogin):
            users.append(SSHUser(entry.user,entry.date))
        else:
            users.append(entry)

    for user in users:
        print(str(user.validate())+str(user))


