import sys
import re
import datetime

def parseRequest(requestLine):
    requestParameters = requestLine.strip().split()
    return requestParameters




def getConvertedDatetime(requestParameters):
    return datetime.datetime(
        getYear(requestParameters),
        getMonthNumber(requestParameters),
        getDayOfMonth(requestParameters),
        getHourOfTimestamp(requestParameters),
        getMinuteOfTimestamp(requestParameters),
        getSecondOfTimestamp(requestParameters)
        )

def convertRequestParametersToTuple(requestParameters):
    #Convert date to datetime.datetime
    #validateRequestParameters(requestParameters)
    
    return (getHostname(requestParameters), 
            getConvertedDatetime(requestParameters), 
            getRequestType(requestParameters),
            getPath(requestParameters),
            getProtocol(requestParameters),
            getStatus(requestParameters),
            getSize(requestParameters)
            )

def validateRequest(requestLine):
   requestParameters = parseRequest(requestLine)
   validateRequestParameters(requestParameters)
   return requestLine

def validateRequestParameters(requestParameters):
    regexPattern = "[^0-9]"

    if(len(requestParameters)!=10 or 
      (re.search(regexPattern,requestParameters[9]) and requestParameters[8]=="200")
        or re.search(regexPattern,requestParameters[8]) or len(re.split(":",requestParameters[3][1:]))<1):
        raise ValueError(f"Incorrectly formated data [{len(requestParameters)}] elements: "+str(requestParameters))
    else:
        return requestParameters

def getStatus(requestParameters):
    #validateRequestParameters(requestParameters)
    return int(requestParameters[8])

def getSize(requestParameters):

    #validateRequestParameters(requestParameters)
    if(requestParameters[8]!="200" and requestParameters[9]=="-"):
        return 0
    else:
        return int(requestParameters[9])

def getPath(requestParameters):
    #validateRequestParameters(requestParameters)
    return requestParameters[6]

def getRequestType(requestParameters):
    #validateRequestParameters(requestParameters)
    return requestParameters[5][1:]

def getFileExtension(requestParameters):
    #validateRequestParameters(requestParameters)
    fileExtension= requestParameters[6].split("/")
    if(len(fileExtension)>0):
        fileExtension= fileExtension[-1].split(".")

        if(len(fileExtension)>1):
            return fileExtension[1]
   
    return "Unknown"
    
def isImage(extension):
    
    return (re.search("jpeg$|png$|jpg$", extension))

def getTimestamp(requestParameters):
    #validateRequestParameters(requestParameters)
    return requestParameters[3][1:]

def getParsedTimestamp(requestParameters):
    #validateRequestParameters(requestParameters)
    timestamp = getTimestamp(requestParameters)
    return re.split(":", timestamp)

def getProtocol(requestParameters):
    #validateRequestParameters(requestParameters)
    return requestParameters[7]

def getHourOfTimestamp(requestParameters):
    #validateRequestParameters(requestParameters)
    return int(getParsedTimestamp(requestParameters)[-3])

def getMinuteOfTimestamp(requestParameters):
    #validateRequestParameters(requestParameters)
    return int(getParsedTimestamp(requestParameters)[-2])

def getSecondOfTimestamp(requestParameters):
    #validateRequestParameters(requestParameters)
    return int(getParsedTimestamp(requestParameters)[-1])
    
    
def getDate(requestParameters):
    #validateRequestParameters(requestParameters)
    return getParsedTimestamp(requestParameters)[0]

def getYear(requestParameters):
    #validateRequestParameters(requestParameters)
    return int(getParsedDate(requestParameters)[2])

def getDayOfMonth(requestParameters):
    #validateRequestParameters(requestParameters)
    return int(getParsedDate(requestParameters)[0])


def getParsedDate(requestParameters):
    #validateRequestParameters(requestParameters)
    return getDate(requestParameters).split("/")

def getMonthNumber(requestParameters):
    #validateRequestParameters(requestParameters)
    monthName = getParsedDate(requestParameters)[1]
    match monthName:
        case "Jan":
            return 0
        case "Feb":
            return 1
        case "Mar":
            return 2
        case "Apr":
            return 3
        case "May":
            return 4
        case "Jun":
            return 5
        case "Jul":
            return 6
        case "Aug":
            return 7
        case "Sep":
            return 8
        case "Oct":
            return 9
        case "Nov":
            return 10
        case "Dec":
            return 11


def getDayOfWeek(requestParameters):
    #validateRequestParameters(requestParameters)
    parsedDate = getParsedDate(requestParameters)
    date = datetime.date(int(parsedDate[2]), getMonthNumber(parsedDate[1]), int(parsedDate[0]))
    return date.weekday()


def getHostname(requestParameters):
    #validateRequestParameters(requestParameters)
    return requestParameters[0]

def getHostDomain(requestParameters):
    #validateRequestParameters(requestParameters)
    return getHostname(requestParameters).split(".")[-1]