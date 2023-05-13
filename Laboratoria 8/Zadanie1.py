import abc
from logUtils import *
from parsingUtils import *
from ipaddress import *

class SSHLogEntry(metaclass=abc.ABCMeta):
   def  __init__(self,rawLog:str):
      #self.__ntLog:GenericLog = convertLineToNamedtuple(logLine)
      self._rawLog = rawLog

   @property
   def date(self):
      return convertLineToNamedtuple(self._rawLog).date
   
   @abc.abstractmethod
   def validate(self):
      pass

   def rawLog(self):
      return self._rawLog
   
   @property
   def pid(self):
      return re.search(PID_PATTERN, convertLineToNamedtuple(self._rawLog).protocol).group(0)
   
   @property
   def ip(self):
      
      ipAddresses: list = getIpv4sFromLog(convertLineToNamedtuple(self._rawLog))
      return  ipAddresses[0] if ipAddresses else None
   
   @property
   def importance(self):
      return (convertLineToNamedtuple(self._rawLog)).message

   @property
   def user(self):
      return getUserFromLog(convertLineToNamedtuple(self._rawLog))
   
   def _validateSSHLogEntry(self, other):
      if not isinstance(other, SSHLogEntry):
         raise Exception("Comparison to other classes is not supported")

   
   @property
   def has_ip(self):
      return True if self.ip else False
   
   def __str__(self):
      return f"Data rządania: {self.date}, użytkownik: {self.user}, adres ip: {self.ip}\n{self._rawLog}\n"
   def __repr__(self):
      return f"DATE: {self.date},HOST: {self.user},PID: {self.pid},IP: {self.ip}"
   
   def __lt__(self, other):
      self._validateSSHLogEntry(other)
      if(self.importance<other.importance):
         return True
      elif(self.importance==other.importance):
         if(simpleDateComparator(self.date, other.date)==-1):
            return True
         else:
            return False
         
      else:
         return False
      
   
   def __eq__(self,other):
      self._validateSSHLogEntry(other)
      
      return not self>other and not self<other

   def __gr__(self,other):
      self._validateSSHLogEntry(other)
      if(self.importance>other.importance):
         return True
      elif(self.importance==other.importance):
         if(simpleDateComparator(self.date, other.date)==1):
            return True
         else:
            return False
         
      else:
         return False

      
class SSHLogClientDetails(SSHLogEntry,metaclass=abc.ABCMeta):

   def __init__(self, logLine:str):
      super().__init__(logLine)

   @property   
   def userPort(self):
      return getUserPort(convertLineToNamedtuple(self._rawLog)).group(0)

   

class SSHLogLogin(SSHLogClientDetails,metaclass=abc.ABCMeta):

   def __init__(self, logLine:str):
      super().__init__(logLine)
   
   @property
   def userProtocol(self):
      return getClientProtocol(convertLineToNamedtuple(self._rawLog)).group(0)


class SSHLogFailedPassword(SSHLogLogin):
   
   def __init__(self, logLine:str):
      super().__init__(logLine)

   @property
   def isUserInvalid(self):
      return bool(re.search(INVALID_USER_PATTERN,(convertLineToNamedtuple(self._rawLog)).message))
     
      
   def validate(self):
      return getMessageFromLog(self._rawLog)!=MESSAGE_TYPE.WRONG_PASSWORD
   
   def __str__(self):
      return ("Type: "+MESSAGE_TYPE.WRONG_PASSWORD.name)+super().__str__()

   

class SSHLogAcceptedPassword(SSHLogLogin):
   
   def __init__(self, logLine:str):
      super().__init__(logLine)
     
      
   def validate(self):
      return getMessageFromLog(self._rawLog)!=MESSAGE_TYPE.SUCCESSFUL_LOGIN
   
   def __str__(self):
      return  ("Type: "+MESSAGE_TYPE.SUCCESSFUL_LOGIN.name)+super().__str__()

         
class SSHLogError(SSHLogClientDetails):
    def __init__(self, logLine:str):
      super().__init__(logLine)


    @property
    def reasonForError(self):
      return convertLineToNamedtuple(self._rawLog).message.split(":")[-1]
     
      
    def validate(self):
      return getMessageFromLog(self._rawLog)!=MESSAGE_TYPE.ERROR
    
    def __str__(self):
      return ("Type: "+MESSAGE_TYPE.ERROR.name)+super().__str__()
   
    

class SSHLogOther(SSHLogEntry):
    def __init__(self, logLine:str):
      super().__init__(logLine)
     
      
    def validate(self):
      return True
    
    def __str__(self):
      return ("Type: "+MESSAGE_TYPE.OTHERS.name)+"\n"+super().__str__()
   


