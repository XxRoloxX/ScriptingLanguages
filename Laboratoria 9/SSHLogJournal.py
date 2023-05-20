import abc
from Zadanie1 import SSHLogAcceptedPassword, SSHLogEntry, SSHLogError, SSHLogFailedPassword, SSHLogOther
from logUtils import *
from typing import *

LOG_LIST_ATTRIBUTE:str = "_logList"
FILTER_METHOD_NAME:str = "filterSSHLogJournal"


class SSHLogJournal(object):

    def __init__(self:'SSHLogJournal', *args:List['SSHLogEntry']):

        if (len(args) == 1 and isinstance(args, object)):
            self._logList :List['SSHLogEntry'] = []
            for el in args[0]:
                if (isinstance(el, SSHLogEntry) and el.validate()):
                    self._logList.append(el)
        else:
            self._logList = []

    def _getCreator(self:'SSHLogJournal', newRawlog:str) -> 'SSHLogCreator':
        logType :MESSAGE_TYPE = getMessageFromLog(convertLineToNamedtuple(newRawlog))
        match logType:
            case MESSAGE_TYPE.SUCCESSFUL_LOGIN:
                return SSHLogAcceptedPasswordCreator()
            case MESSAGE_TYPE.WRONG_PASSWORD:
                return SSHLogFailedPasswordCreator()
            case MESSAGE_TYPE.ERROR:
                return SSHLogErrorCreator()
            case _:
                return SSHLogOtherCreator()

    def append(self:'SSHLogJournal', newRawLog: str)->None:
        creator:'SSHLogCreator' = self._getCreator(newRawLog)
        newLog:'SSHLogEntry' = creator.createLog(newRawLog)

        if newLog.validate():
            object.__getattribute__(self, LOG_LIST_ATTRIBUTE).append(newLog)
        else:
            raise Exception("Not appropriate log record")

    def filterSSHLogJournal(self:'SSHLogJournal', filterMethod: Callable[['SSHLogEntry'], bool])->'SSHLogJournal':

        filteredList: List['SSHLogEntry'] = list(filter(
            filterMethod, object.__getattribute__(self, LOG_LIST_ATTRIBUTE)))
        return SSHLogJournal(filteredList)

    def filterSSHLogJournalBasedOnIP(self:'SSHLogJournal', ip:str) ->'SSHLogJournal':
        return self.filterSSHLogJournal(lambda log: log.ip == ip)

    def __len__(self:'SSHLogJournal')->int:
        return len(self._logList)

    def __iter__(self:'SSHLogJournal')->Iterator['SSHLogEntry']:
        return iter(self._logList)

    def __contains__(self, element:str)->bool:
        return element in self._logList

    def getSortedJournal(self:'SSHLogJournal')->'SSHLogJournal':
        return SSHLogJournal(sorted(self._logList))

    def __getattr__(self:'SSHLogJournal', attr: str)->Any:
        return object.__getattribute__(self, FILTER_METHOD_NAME)(lambda log: attr in log._rawLog)

    def __getitem__(self:'SSHLogJournal', item:Union[slice,str])->Any:
        if isinstance(item, slice):
            return SSHLogJournal(object.__getattribute__(self, LOG_LIST_ATTRIBUTE)[item.start:item.stop:item.step])
        else:
            return self.__getattr__(item)
        
    def get(self, index):
        if index<0 or index>=len(self._logList):
            return None
        else:
            return self._logList[index]

class SSHLogCreator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createLog(self, rawLog:str)->'SSHLogEntry':
        pass


class SSHLogFailedPasswordCreator(SSHLogCreator):
    def createLog(self, rawLog:str)->'SSHLogEntry':
        return SSHLogFailedPassword(rawLog)


class SSHLogAcceptedPasswordCreator(SSHLogCreator):
    def createLog(self, rawLog:str)->'SSHLogAcceptedPassword':
        return SSHLogAcceptedPassword(rawLog)


class SSHLogErrorCreator(SSHLogCreator):
    def createLog(self, rawLog:str)->'SSHLogError':
        return SSHLogError(rawLog)


class SSHLogOtherCreator(SSHLogCreator):
    def createLog(self, rawLog:str)->'SSHLogOther':
        return SSHLogOther(rawLog)
