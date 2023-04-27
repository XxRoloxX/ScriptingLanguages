from collections import namedtuple
import datetime
import random
import statistics

INITIAL_YEAR=1900

SessionTime = namedtuple("SessionTime", "sessionStart sessionEnd")

def getMonthNumber(name):
    #validateRequestParameters(requestParameters)
    match name:
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

def getNRandomInts(n,min,max):
    if max-min+1 < n:
        raise Exception("To less range for given n")
    
    accum = []
    while len(accum)<n:
        newRandom = random.randint(min,max)
        if newRandom not in accum:
            accum.append(newRandom)
    
    return accum
#Accepts SimpleTime, returns datetime.datetime object
def getTimeDifference(start, end):
    startDate = datetime.datetime(INITIAL_YEAR,start.month+1,start.day,start.hour,start.minute,start.second)
    endDate = datetime.datetime(INITIAL_YEAR,end.month+1,end.day,end.hour,end.minute,end.second)
    return(endDate - startDate)*1

def getStatisticsFromArray(array):
    result = dict()
    result["mean"] = round(statistics.mean(array),2)
    result["stdev"] = round(statistics.stdev(array),2)

    return result   

def getRandomKeyFromDictionary(dictionary:dict):
    keyIndex = random.randint(0, len(dictionary.keys()))
    choosenKey = list(dictionary.keys())[keyIndex]
    return choosenKey

def filterDictionary(dictionary:dict, filterFunction):
    filteredDictionary = dict()

    for key,value in dictionary.items():
        if filterFunction(value):
            filteredDictionary[key]=value
    
    return filteredDictionary

def getMaxAndMinItemsInDictionary(dictionary:dict):

    maxKey=[]
    maxValue=0

    minKey=[]
    minValue=0

    firstMinAssigment=False
    firstMaxAssigment=False

    for key,value in dictionary.items():

        if not firstMinAssigment:
            minKey=[key]
            minValue=value
            firstMinAssigment=True
        elif minValue>value:
            minValue=value
            minKey=[key]
        elif minValue==value:
            minKey+=key

        if not firstMaxAssigment:
            maxKey=[key]
            maxValue=value
            firstMaxAssigment=True
        elif maxValue<value:
            maxValue=value
            maxKey=[key]
        elif maxValue==value:
            maxKey+=[key]

    return {
        
        "mostPopularKey": maxKey,
        "maxAmount":maxValue,
        "leastPopularKey":minKey,
        "minAmount":minValue
        
    }
        

def getCallable(function,*args):
    

    def callableFunction():
        return function(*args)
    
    return callableFunction

