from collections import namedtuple
import datetime
from enum import Enum
import logging
import pprint
import uuid
from parsingUtils import *
import re
import sys

SimpleDate = namedtuple("SimpleDate", "month day hour minute second")
GenericLog = namedtuple("GenericLog","date host protocol message")
SessionTime = namedtuple("SessionTime", "sessionStart sessionEnd")

DEFAULT_LOG_LEVEL=logging.DEBUG

IP_ADDRESS_RE_PATTERN = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
USER_RE_PATTERN = r"(?<=user[=\s])\b\w+\b(?<!request)(?<!authentication)|Accepted password for (\b\w+\b)"
PID_PATTERN = r"\d+"
INVALID_USER_PATTERN = r"(Invalid user)"

CORRECT_USER_PATTERN = r'^[a-z_][a-z0-9_-]{0,31}$'

SUCCESSFUL_LOGIN_PATTERN = r"(Accepted password)"
UNSUCCESSFUL_LOGIN_PATTERN = r"(authentication failure)"
SESSION_CLOSED_PATTERN = r"([Ss]ession closed|Received disconnect|Connection closed)"
SESSION_OPENED_PATTERN = r"([Ss]ession opened)"
WRONG_PASSWORD_PATTERN = r"(Failed password)"
WRONG_USERNAME_PATTERN = r"([i,I]nvalid user|user unknown)"
INTRUSION_ATTEMPT_PATTERN= r"(POSSIBLE BREAK-IN ATTEMPT)"
ERROR_PATTERN = r"(error)"
PORT_PATTERN=r"port (\d+)|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}: (\d+)"
CLIENT_PROTOCOL = r"(ssh\d*)"
#BYTES_READ_PATTERN = r"(Bytes read)"




class MESSAGE_TYPE(Enum):
     ERROR=0
     SUCCESSFUL_LOGIN = 1
     UNSUCCESSFUL_LOGIN =2
     SESSION_CLOSED = 3
     SESSION_OPENED =4
     WRONG_PASSWORD = 5
     WRONG_USERNAME = 6
     INTRUSION_ATTEMPT = 7
     OTHERS = 8
    




def getSimpleDate(line:str):
    splitedArguments = re.split("\s+",line)
    #splitedArguments = line.split(" ")
    month = getMonthNumber(splitedArguments[0])
    day = int(splitedArguments[1])

    time = re.split(":",splitedArguments[2]) 
    hour = int(time[0])
    minute = int(time[1])
    second = int(time[2])

    return SimpleDate(month,day,hour,minute,second)

def simpleDateComparator(simpleDate:SimpleDate, otherSimpleDate:SimpleDate):
    return compareObjectsByAttributes(simpleDate,otherSimpleDate,["month","day","hour","minute","second"])


     


def openFile(path,callbacks):
    with open(path) as file:
        line = file.readline()
        while(line!=""):
            for callback in callbacks:
                callback(line)
                     
            line = file.readline()



def convertLineToNamedtuple(line:str):
    
    if line:
     splitedArguments = re.split("\s+",line)
     date = getSimpleDate(" ".join(splitedArguments[:3]))
     host = splitedArguments[3]
     protocol = splitedArguments[4][:-1]
     message = " ".join(splitedArguments[5:])
     return GenericLog(date, host, protocol, message)

def textToNamedTupleAdapter(function):
     def adaptedFunction(line):
          return function(convertLineToNamedtuple(line))

     return adaptedFunction


def validateSSHLog(rawLog):
    try:
        convertLineToNamedtuple(rawLog)
    except Exception:
        raise Exception("Inaproppriate log format")

def getDefaultLoggingMapping(logger):

     return  {
     "SUCCESSFUL_LOGIN": logger.info,
     "SESSION_CLOSED": logger.info,
     "ERROR": logger.error,
     "SESSION_OPENED": logger.info,
     "OTHERS" : logger.debug,
     "UNSUCCESSFUL_LOGIN":logger.warning,
     "WRONG_USERNAME": logger.error,
     "WRONG_PASSWORD": logger.error,
     "INTRUSION_ATTEMPT":logger.critical
     }



def printingDecorator(function, description=""):
     def printingFunction(*arg):
          functionResult = function(*arg)
          print(description+pprint.pformat(functionResult))
          return functionResult
     return printingFunction

def getIpv4sFromLog(logNamedtuple):
        message = logNamedtuple.message
        addresses = re.findall(IP_ADDRESS_RE_PATTERN,message)
        return addresses

def getUserFromLog(logNamedtuple):
     message = logNamedtuple.message
     user = re.search(USER_RE_PATTERN,message)
     if user:
          return user.group(0)
     else:
          return None #If user not found return None
     
def getMessageFromLog(logNamedtuple):
     try:
          message = logNamedtuple.message
     except Exception:
          return MESSAGE_TYPE.OTHERS

     if(re.search(SUCCESSFUL_LOGIN_PATTERN, message)):
          return MESSAGE_TYPE.SUCCESSFUL_LOGIN
     elif(re.search(ERROR_PATTERN,message)):
          return MESSAGE_TYPE.ERROR
     elif(re.search(UNSUCCESSFUL_LOGIN_PATTERN, message)):
          return MESSAGE_TYPE.UNSUCCESSFUL_LOGIN
     elif(re.search(SESSION_CLOSED_PATTERN, message)):
          return MESSAGE_TYPE.SESSION_CLOSED
     elif(re.search(SESSION_OPENED_PATTERN,message)):
          return MESSAGE_TYPE.SESSION_OPENED
     elif(re.search(WRONG_PASSWORD_PATTERN,message)):
          return MESSAGE_TYPE.WRONG_PASSWORD
     elif(re.search(WRONG_USERNAME_PATTERN,message)):
          return MESSAGE_TYPE.WRONG_USERNAME
     elif(re.search(INTRUSION_ATTEMPT_PATTERN,message)):
          return MESSAGE_TYPE.INTRUSION_ATTEMPT
     else:
          return MESSAGE_TYPE.OTHERS
     
def getUserPort(ntLog):
     return re.search(PORT_PATTERN,ntLog.message)

def getClientProtocol(ntLog):
     return re.search(CLIENT_PROTOCOL,ntLog.message)
def logNumberOfBytes(loggerFun:logging):

     size = [0]

     def logNumberOfBytes(line):
          if(len(line)>0):
               size[0]+=len(line)
               loggerFun("Bytes read so far: "+str(size[0]))

     return logNumberOfBytes

def logMessageTypeWithMethod(messageType:MESSAGE_TYPE, loggingMethod,infoMessage=""):

     def logMessageTypeInfoInner(line):
          log = convertLineToNamedtuple(line)
          type = getMessageFromLog(log)
          if(type==messageType):
               loggingMethod(infoMessage+log.message)

     return logMessageTypeInfoInner

#Returns dictionary with users assigned with theirs logs
def groupUsersLogs(): 

     users = dict()

     def accumulateUsersLogs(logNamedtuple):

          if not logNamedtuple:
               return users
          
          user = getUserFromLog(logNamedtuple)

          if user:
               users[user] = users.get(user,[])
               users[user].append(logNamedtuple)

          return users
     
     return accumulateUsersLogs

def logFilter(filterFunction):

     accum =[]

     def logFilterInner(ntLog):

          if(ntLog and filterFunction(ntLog)):
               accum.append(ntLog)
          
          return accum
          
     return logFilterInner

def filterListOfLogs(ntLogsList:list, filterFunction):

    result = []
    for log in ntLogsList:
        if filterFunction(log):
            result.append(log)
    return result

def getRandomUserLogsFromDictionary(usersDictionary:dict):

    keyIndex = random.randint(0, len(usersDictionary.keys()))
    choosenKey = list(usersDictionary.keys())[keyIndex]
    numberOfRecords = random.randint(1, len(usersDictionary[choosenKey]))
    
    logIndexes = getNRandomInts(numberOfRecords,0,len(usersDictionary[choosenKey])-1)
    userLogs = usersDictionary[choosenKey]


    return [userLogs[i] for i in range(0,numberOfRecords) if i in logIndexes]

#Returns list of sessions of given user
def allSessionsOfUser(usersLogs:dict, userKey:str):

    sessions = list()

    userLogs = usersLogs[userKey]

    lastOpenSession = None
    lastClosedSession = None


    for log in userLogs:

        logType= getMessageFromLog(log)

        if logType==MESSAGE_TYPE.SESSION_OPENED:
            lastOpenSession=log
            lastClosedSession = None
        elif logType==MESSAGE_TYPE.SESSION_CLOSED:
            lastClosedSession=log

            if lastClosedSession and lastOpenSession:
                sessions.append(SessionTime(lastOpenSession, lastClosedSession))

            lastOpenSession = None
            lastClosedSession = None

    return sessions

def getUserSessionTimes(usersLogs:dict, userKey:str):
    
    userSessions = allSessionsOfUser(usersLogs, userKey)    

    userSessionTimes = [getTimeDifference(session.sessionStart.date, session.sessionEnd.date) for session in userSessions]

    return userSessionTimes



def getAllSessionTimes(usersLogs:dict):
    sessionTimes = []
    

    for user in usersLogs.keys():

        userSessionTimes = getUserSessionTimes(usersLogs, user)

        if userSessionTimes:
             sessionTimes+=userSessionTimes

    return sessionTimes

def getStatisticsFromAllLogs(usersLogs:dict()):

    sessionTimes = getAllSessionTimes(usersLogs)
    #print(sessionTimes)
    sesssionTimesInSeconds = [(sessionTime).seconds for sessionTime in sessionTimes]

    return getStatisticsFromArray(sesssionTimesInSeconds)

def getStatisticsForEachUser(usersLogs:dict()):

    result = dict()

    for user,logs in usersLogs.items():

        userSessionTimes = getUserSessionTimes(usersLogs,user)

        if len(userSessionTimes)>=2:
            userSessionTimesInSeconds = [(sessionTime).seconds for sessionTime in userSessionTimes]
            result[user] = getStatisticsFromArray(userSessionTimesInSeconds)

    return result



def getNumberOfLogsTypeForEachUser(usersLogs:dict, filterFunction):

    usersLoginsAttempts = dict()

    for user,logs in usersLogs.items():
        #print(getMessageFromLog(log))
        filteredLogs = filterListOfLogs(logs,filterFunction)
        #filteredLogs = filterListOfLogs(logs,lambda log:  True)
        if filteredLogs:
            usersLoginsAttempts[user] = len(filteredLogs)
    
    return usersLoginsAttempts

def getLoggingFunction(configurationJSON):

     def getLoggingFunctionInner(messageType):
          #print("debug: "+str(value))
          returnFunction = configurationJSON[messageType.name]
          return returnFunction
     return getLoggingFunctionInner


def defaultLoggingDecorator(function, minLevel, infoBeforeLog="%(levelname)s"):
     logger = configureLogging(minLevel,infoBeforeLog)
     loggingFunctionGetter = getLoggingFunction(getDefaultLoggingMapping(logger))

     def loggingDecoratorInner(ntLog):
          result = function(ntLog)
          loggingFunction  = loggingFunctionGetter(getMessageFromLog(ntLog))
          
          loggingFunction(result)
          return result
     
     return loggingDecoratorInner

def configureLogging(minLevel=logging.DEBUG, infoBeforeLog="%(levelname)s"):
    #logging.basicConfig(level=logging.NOTSET)
    formatter = logging.Formatter(infoBeforeLog+': %(message)s')
    #Default level is WARNING (so nothing above WARNING (DEBUG, INFO) will be logged)
    logger = logging.getLogger(str(uuid.uuid1()))
    logger.setLevel(minLevel)

    #Handlers are the children of the logger (level of their parent applies to them too, if level of parent is ERROR, then they wont recieve any DEBUGS, INFO, ect.)
    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)


    normal_handler = logging.StreamHandler(sys.stdout)
    normal_handler.setFormatter(formatter)
    #setLevel is not needed because by default it is NOTSET, so their parent's level will be assigned 
    normal_handler.addFilter(logAboveLevel(logging.WARNING))
    
    
    logger.addHandler(normal_handler)
    logger.addHandler(error_handler)

    
    return logger
    
          
def logAboveLevel(level:logging):
    def logAboveLevelInner(record):
        if record.levelno <= level:
            return 1
        else:
            return 0
    return logAboveLevelInner

          
                    

