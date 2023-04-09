import pprint
import statistics
from logUtils import *
import random
from parsingUtils import *


def getNRandomLogsFromUser(userLogs:list, numberOfLogsToReturn:int):


    if len(userLogs)>=numberOfLogsToReturn:
        logIndexes = getNRandomInts(numberOfLogsToReturn,0,len(userLogs)-1)
        return [userLogs[i] for i in range(0,len(userLogs)) if i in logIndexes]
    else:
        return False



#Returns random number of logs from random user
def getRandomUserLogsFromDictionary(usersDictionary:dict, numberOfLogsToReturn:int):

    filteredUserDictionary = filterDictionary(usersDictionary, lambda logs: len(logs)>=numberOfLogsToReturn)

    if not filteredUserDictionary:
        raise Exception("Number of Logs to return is higher than number of logs of any user")

    randomKey = getRandomKeyFromDictionary(filteredUserDictionary)

    randomLogs = getNRandomLogsFromUser(filteredUserDictionary[randomKey],numberOfLogsToReturn)

    while not randomLogs:
        randomLogs = getNRandomLogsFromUser(filteredUserDictionary[randomKey],numberOfLogsToReturn)

    return randomLogs

def getUsersWithMostLoginAttempts(usersDictionary:dict):

    numberOfLogsForEachUser = getNumberOfLogsTypeForEachUser(usersDictionary, 
                                                             lambda log: getMessageFromLog(log)==MESSAGE_TYPE.SUCCESSFUL_LOGIN or getMessageFromLog(log)==MESSAGE_TYPE.UNSUCCESSFUL_LOGIN)
    return getMaxAndMinItemsInDictionary(numberOfLogsForEachUser)


if __name__=="__main__":
    accumulationFunction = groupUsersLogs()
    

    openFile("SSH/SSH.log", [ textToNamedTupleAdapter(accumulationFunction),
                              
                              ])
    
    dUsersWithLogsDictionary = accumulationFunction(None)

    # a)                           
    pprint.pprint(getRandomUserLogsFromDictionary(dUsersWithLogsDictionary,5))
    # b)
    pprint.pprint(getStatisticsFromAllLogs(dUsersWithLogsDictionary))
    # c)
    pprint.pprint(getStatisticsForEachUser(dUsersWithLogsDictionary))
    # d)
    pprint.pprint(getUsersWithMostLoginAttempts(dUsersWithLogsDictionary))
