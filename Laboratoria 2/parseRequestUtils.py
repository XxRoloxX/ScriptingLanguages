import sys
import re
import datetime

def parseRequest(requestLine):
    requestParameters = requestLine.strip().split()
    return requestParameters


def validateRequest(requestLine):
   requestParameters = parseRequest(requestLine)
   regexPattern = "[^0-9]"

   if(len(requestParameters)!=10 or 
      (re.search(regexPattern,requestParameters[9]) and requestParameters[8]=="200")
        or re.search(regexPattern,requestParameters[8]) or len(getParsedTimestamp(requestParameters))<1):
        raise Exception(f"Incorrectly formated data [{len(requestParameters)}] elements: "+str(requestLine.strip().split(" ")))
   else:
        return requestLine
        
def getStatus(requestParameters):
    return requestParameters[8]

def getSize(requestParameters):
    if(requestParameters[8]!="200" and requestParameters[9]=="-"):
        return 0
    else:
        return int(requestParameters[9])

def getPath(requestParameters):
    return requestParameters[6]

def getFileExtension(requestParameters):
    fileExtension= requestParameters[6].split("/")
    if(len(fileExtension)>0):
        fileExtension= fileExtension[len(fileExtension)-1].split(".")
    if(len(fileExtension)>1):
        return fileExtension[1]
    else:
        return "Unknown"
    
def isImage(extension):
    return (re.search("jpeg$|png$|jpg$", extension))

def getTimestamp(requestParameters):
    return requestParameters[3][1:]

def getParsedTimestamp(requestParameters):
    timestamp = getTimestamp(requestParameters)
    return re.split(":", timestamp)
    

def getHourOfTimestamp(requestParameters):
    timestamp = getParsedTimestamp(requestParameters)
    return timestamp[-3]
    
def getDate(requestParameters):
    return getParsedTimestamp(requestParameters)[0]

def getParsedDate(requestParameters):
    return getDate(requestParameters).split("/")

def getMonthNumber(monthName):
    monthName = monthName[0:3]
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
    parsedDate = getParsedDate(requestParameters)
    date = datetime.date(int(parsedDate[2]), getMonthNumber(parsedDate[1]), int(parsedDate[0]))
    return date.weekday()


def getHostname(requestParameters):
    return requestParameters[0]

def getHostDomain(requestParameters):
    return getHostname(requestParameters).split(".")[-1]