import abc
from logUtils import *
from parsingUtils import *
from ipaddress import *
from typing import *
from re import *

class SSHLogEntry(metaclass=abc.ABCMeta):
   def  __init__(self:'SSHLogEntry',rawLog:str)->None:
      #self.__ntLog:GenericLog = convertLineToNamedtuple(logLine)
      self._rawLog:str = rawLog

   @property
   def date(self:'SSHLogEntry')->'SimpleDate':
      return convertLineToNamedtuple(self._rawLog).date
   
   @abc.abstractmethod
   def validate(self:'SSHLogEntry')->bool:
      pass

   @property
   def getRawLog(self:'SSHLogEntry')->str:
      return self._rawLog
   
   @property
   def pid(self:'SSHLogEntry')->Union[str,None]:
      pidResult: Union[Match[str],None] = re.search(PID_PATTERN, convertLineToNamedtuple(self._rawLog).protocol)
      if pidResult:
         return pidResult.group(0)
      else:
         return None
   
   @property
   def ip(self:'SSHLogEntry')->Union[str,None]:
      
      ipAddresses: List[str] = getIpv4sFromLog(convertLineToNamedtuple(self._rawLog))
      return  ipAddresses[0] if ipAddresses else None
   
   @property
   def importance(self:'SSHLogEntry')->'GenericLog':
      return (convertLineToNamedtuple(self._rawLog)).message

   @property
   def user(self:'SSHLogEntry')->Union[str,None]:
      return getUserFromLog(convertLineToNamedtuple(self._rawLog))
   
   def _validateSSHLogEntry(self:'SSHLogEntry', other:object)->None:
      if not isinstance(other, SSHLogEntry):
         raise Exception("Comparison to other classes is not supported")

   
   @property
   def has_ip(self:'SSHLogEntry')->bool:
      return True if self.ip else False
   
   def __str__(self:'SSHLogEntry')->str:
      return f"Data rządania: {self.date}, użytkownik: {self.user}, adres ip: {self.ip}\n{self._rawLog}\n"
   
   def __repr__(self:'SSHLogEntry')->str:
      return f"DATE: {self.date},HOST: {self.user},PID: {self.pid},IP: {self.ip}"
   
   def __lt__(self:'SSHLogEntry', other:object)->bool:
      
      if(isinstance(other, SSHLogEntry)):
         if(self.importance<other.importance):
            return True
         elif(self.importance==other.importance):
            if(simpleDateComparator(self.date, other.date)==-1):
               return True
            else:
               return False
         else:
            return False
      else:
         raise Exception("Comparison to other classes is not supported")
         
      
   def __eq__(self:'SSHLogEntry',other:object)->bool:
      
      if(isinstance(other,SSHLogEntry)):
         return not self>other and not self<other
      else:
         raise Exception("Comparison to other classes is not supported")

   def __gr__(self:'SSHLogEntry',other:object)->bool:
      self._validateSSHLogEntry(other)
      if(isinstance(other,SSHLogEntry)):
         if(self.importance>other.importance):
            return True
         elif(self.importance==other.importance):
            if(simpleDateComparator(self.date, other.date)==1):
               return True
            else:
               return False
         else:
            return False
         
      else:
         return False

      
class SSHLogClientDetails(SSHLogEntry,metaclass=abc.ABCMeta):

   def __init__(self:'SSHLogClientDetails', logLine:str)->None:
      super().__init__(logLine)

   @property   
   def userPort(self:'SSHLogClientDetails')->str:
      return getUserPort(convertLineToNamedtuple(self._rawLog)).group(0)

   

class SSHLogLogin(SSHLogClientDetails,metaclass=abc.ABCMeta):

   #def __init__(self:'SSHLogClientDetails', logLine:str)->None:
   #   super().__init__(logLine)
   #   print(logLine)
   
   @property
   def userProtocol(self:'SSHLogClientDetails')->str:
      return getClientProtocol(convertLineToNamedtuple(self._rawLog)).group(0)


class SSHLogFailedPassword(SSHLogLogin):
   
   def __init__(self:'SSHLogFailedPassword', logLine:str)->None:
      super().__init__(logLine)

   @property
   def isUserInvalid(self:'SSHLogFailedPassword')->bool:
      return bool(re.search(INVALID_USER_PATTERN,(convertLineToNamedtuple(self._rawLog)).message))
     
      
   def validate(self:'SSHLogFailedPassword')->bool:
      return getMessageFromLog(self._rawLog)!=MESSAGE_TYPE.WRONG_PASSWORD
   
   def __str__(self:'SSHLogFailedPassword')->str:
      return ("Type: "+MESSAGE_TYPE.WRONG_PASSWORD.name)+super().__str__()

   

class SSHLogAcceptedPassword(SSHLogLogin):
   
   def __init__(self:'SSHLogAcceptedPassword', logLine:str)->None:
      super().__init__(logLine)
     
      
   def validate(self:'SSHLogAcceptedPassword')->bool:
      return getMessageFromLog(self._rawLog)!=MESSAGE_TYPE.SUCCESSFUL_LOGIN
   
   def __str__(self:'SSHLogAcceptedPassword')->str:
      return  ("Type: "+MESSAGE_TYPE.SUCCESSFUL_LOGIN.name)+super().__str__()

         
class SSHLogError(SSHLogClientDetails):
    def __init__(self:'SSHLogError', logLine:str)->None:
      super().__init__(logLine)


    @property
    def reasonForError(self:'SSHLogError')->str:
      return convertLineToNamedtuple(self._rawLog).message.split(":")[-1]
     
      
    def validate(self:'SSHLogError')->bool:
      return getMessageFromLog(self._rawLog)!=MESSAGE_TYPE.ERROR
    
    def __str__(self:'SSHLogError')->str:
      return ("Type: "+MESSAGE_TYPE.ERROR.name)+super().__str__()
   
    

class SSHLogOther(SSHLogEntry):
    def __init__(self:'SSHLogOther', logLine:str)->None:
      super().__init__(logLine)
     
      
    def validate(self:'SSHLogOther')->Literal[True]:
      return True
    
    def __str__(self:'SSHLogOther')->str:
      return ("Type: "+MESSAGE_TYPE.OTHERS.name)+"\n"+super().__str__()
   

def get_log_entry(raw_log:str)->'SSHLogEntry':
   log_type = getMessageFromLog(raw_log)

   if log_type==MESSAGE_TYPE.SUCCESSFUL_LOGIN:
      return SSHLogAcceptedPassword(raw_log)
   elif log_type==MESSAGE_TYPE.WRONG_PASSWORD:
      return SSHLogFailedPassword(raw_log)
   elif log_type==MESSAGE_TYPE.ERROR:
      return SSHLogError(raw_log)
   else:
      return SSHLogOther(raw_log)