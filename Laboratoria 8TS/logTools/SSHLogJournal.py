import abc
from Zadanie1 import SSHLogAcceptedPassword, SSHLogEntry, SSHLogError, SSHLogFailedPassword, SSHLogOther
from logUtils import *

LOG_LIST_ATTRIBUTE = "_logList"
FILTER_METHOD_NAME = "filterSSHLogJournal"


class SSHLogJournal(object):

    def __init__(self, *args):

        if (len(args) == 1 and isinstance(args, object)):
            self._logList = []
            for el in args[0]:
                if (isinstance(el, SSHLogEntry) and el.validate()):
                    self._logList.append(el)
        else:
            self._logList = []

    def _getCreator(self, newRawlog):
        logType = getMessageFromLog(convertLineToNamedtuple(newRawlog))
        match logType:
            case MESSAGE_TYPE.SUCCESSFUL_LOGIN:
                return SSHLogAcceptedPasswordCreator()
            case MESSAGE_TYPE.WRONG_PASSWORD:
                return SSHLogFailedPasswordCreator()
            case MESSAGE_TYPE.ERROR:
                return SSHLogErrorCreator()
            case _:
                return SSHLogOtherCreator()

    def append(self, newRawLog: str):
        creator = self._getCreator(newRawLog)
        newLog = creator.createLog(newRawLog)

        if newLog.validate():
            object.__getattribute__(self, LOG_LIST_ATTRIBUTE).append(newLog)
        else:
            raise Exception("Not appropriate log record")

    def filterSSHLogJournal(self, filterMethod):

        filteredList = filter(
            filterMethod, object.__getattribute__(self, LOG_LIST_ATTRIBUTE))
        return SSHLogJournal(filteredList)

    def getListOfRawLogs(self):
        return [log.rawLog for log in self._logList]

    def filterSSHLogJournalBasedOnIP(self, ip):
        return self.filterSSHLogJournal(lambda log: log.ip == ip)

    def __len__(self):
        return len(self._logList)

    def __iter__(self):
        return iter(self._logList)

    def __contains__(self, element):
        return element in self._logList

    def getSortedJournal(self):
        return SSHLogJournal(sorted(self._logList))

    def __getattr__(self, attr: str):
        return object.__getattribute__(self, FILTER_METHOD_NAME)(lambda log: attr in log._rawLog)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return SSHLogJournal(object.__getattribute__(self, LOG_LIST_ATTRIBUTE)[item.start:item.stop:item.step])
        else:
            return self.__getattr__(item)
    

class SSHLogCreator(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def createLog(self, rawLog):
        pass


class SSHLogFailedPasswordCreator(SSHLogCreator):
    def createLog(self, rawLog):
        return SSHLogFailedPassword(rawLog)


class SSHLogAcceptedPasswordCreator(SSHLogCreator):
    def createLog(self, rawLog):
        return SSHLogAcceptedPassword(rawLog)


class SSHLogErrorCreator(SSHLogCreator):
    def createLog(self, rawLog):
        return SSHLogError(rawLog)


class SSHLogOtherCreator(SSHLogCreator):
    def createLog(self, rawLog):
        return SSHLogOther(rawLog)
