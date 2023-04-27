import logging
import sys
from time import time
import uuid


def getLoggingMethod(logger):
    return  {
    "DEBUG": logger.debug,
    "WARNING": logger.warning,
    "INFO": logger.info,
    "ERROR": logger.error,
    "CRITICAL": logger.error,
    }

def getExecutionLog(function, *args, **kvargs):

    startTime,finishTime, returnedValue = timeFunctionExecution(function, *args,**kvargs)
    
    return {
        "resultString": ("Start date: "+str(startTime)\
                        +",exec time: "+str(finishTime-startTime)\
                            +",args: "+str(args)\
                            +", return value: "+str(returnedValue)),
        "startTime" :startTime,
        "finishTime": finishTime,
        "returnedValue": returnedValue
    }


def setUpDefaultLogger():
    logger = logging.getLogger(str(uuid.uuid1()))
    logger.setLevel(logging.DEBUG)
    normal_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    normal_handler.setFormatter(formatter)
    logger.addHandler(normal_handler)
    return logger


def timeFunctionExecution(function, *args, **kvargs):
     startTime = time()
     print(str(args), " "+str(kvargs))
     returnedValue = function(*args)
     finishTime = time()
     return startTime,finishTime,returnedValue


def log(loggingLevel, loggingBehaviour):

    logger = setUpDefaultLogger()

    def wrapper(function):
            
        def decoratedFunction(*args, **kvarg):
            loggingMethod = getLoggingMethod(logger)[loggingLevel]
            resultBehaviorObject = loggingBehaviour(function, *args,**kvarg)
            loggingMethod(resultBehaviorObject["resultString"])
            return resultBehaviorObject["returnedValue"] if "returnedValue" in resultBehaviorObject else None
            
        return decoratedFunction
    return wrapper

def getObjectCreatationNotification(object):

    def innerObjectCreationNotification(function, *args, **kvargs):
        return {"resultString": "Object of type "+str(object.__name__)+" was created"}

    return innerObjectCreationNotification

def logClass(loggingLevel):

    logger = setUpDefaultLogger()
    loggingMethod = getLoggingMethod(logger)[loggingLevel]

    def wrapper(classObject):
        classObject.__init__ = log(loggingLevel, getObjectCreatationNotification(classObject))(classObject.__init__)
        
        return classObject
    
    return wrapper


@logClass("DEBUG")
class BaseClass:
    pass

@log("ERROR", getExecutionLog)
def baseFunction(x,y):
    return x*y

if __name__=="__main__":

    baseFunction(2,4)
    BaseClass()
    BaseClass()
    BaseClass()
    BaseClass()



