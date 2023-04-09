from get_entries import *
from parseTuples import *

def entry_to_dict(tuple):
    
    return {
        TupleElements.ADDRESS.name: getTupleAddr(tuple),
        TupleElements.DATE.name: getTupleDate(tuple),
        TupleElements.MESSAGE.name: getTupleMessage(tuple),
        TupleElements.FILEPATH.name: getTupleFilepath(tuple),
        TupleElements.PROTOCOL.name: getTupleProtocol(tuple),
        TupleElements.CODE.name: getTupleCode(tuple),
        TupleElements.TRANSFERSIZE.name: getTupleTransferSize(tuple)
    }



def universal_log_to_dict(tuples, elementToCompare: TupleElements):
    result = dict()

    for tup in tuples:
        tup_dict = entry_to_dict(tup)
        result[tup_dict[elementToCompare.name]] = result.get(tup_dict[elementToCompare.name],[tup_dict])+[tup_dict]

    return result

def log_to_dict(tuples):
    return universal_log_to_dict(tuples, TupleElements.ADDRESS)


def get_keys(dictionary:dict):
    return list(dictionary.keys())

def get_addr(dictionary:dict):
    return get_keys(dictionary)


def universalDictionaryComparator(elementToCompare: TupleElements):
    def comparator(dictionary):
        return dictionary[elementToCompare.name]
    return comparator


def getInfoAboutHost(dictionaryValues: list):

    host = dictionaryValues[0][TupleElements.ADDRESS.name]
    numberOfRequests = len(dictionaryValues)
    numberOfSuccesfulRequests = len([request for request in dictionaryValues if request[TupleElements.CODE.name]==200])
    sortedDictionaryValues = sorted(dictionaryValues, key=universalDictionaryComparator(TupleElements.DATE))
    oldestRequest = sortedDictionaryValues[0][TupleElements.DATE.name]
    newestRequest = sortedDictionaryValues[-1][TupleElements.DATE.name]
    succesfulRequestsRatio = numberOfSuccesfulRequests/numberOfRequests

    return {
        "host": host,
        "numberOfRequests": numberOfRequests,
        "firstRequest": oldestRequest,
        "lastRequest": newestRequest,
        "ratio": succesfulRequestsRatio
    }

def formatHostData(hostDictionary):

    return "Host: "+hostDictionary["host"] + "\n" +\
           "Number of requests: " +str(hostDictionary["numberOfRequests"]) + "\n"+\
           "First request: " +str(hostDictionary["firstRequest"]) + "\n"+\
           "Last request: " +str(hostDictionary["lastRequest"]) + "\n"+\
           "Succesfull requests ratio: "+str(round(hostDictionary["ratio"]*100,2)) + "%\n"
            


def print_dict_entry_dates(dictionary):

    for key in get_addr(dictionary):
        hostInfo = getInfoAboutHost(dictionary[key])
        formatedData = formatHostData(hostInfo)
        writeToStandardOutput(formatedData)

if __name__=="__main__":
    print_dict_entry_dates(log_to_dict(get_entries_by_extension(read_log(),"")))



