from parseTuples import *
from read_log import *
from enum import Enum
import re


class ListReturnKind(Enum):
    COMBINED = 1
    SEPARATED = 2



def get_entries_by_index(parameterToCompare: TupleElements):
    def get_entries_by_index_inner(tuples, regexToMatch):
        if len(tuples)>0 and len(tuples[0])>parameterToCompare.value:
            return [tup for tup in tuples if re.search(regexToMatch,str(tup[parameterToCompare.value]))]
        else:
            raise Exception("Index out of bounds for tuple" + str(tuples))
    return get_entries_by_index_inner


def get_entries_by_code(tuples, code):
    return get_entries_by_index(TupleElements.CODE)(tuples,code)

def get_entries_by_addr(tuples, addr):
    return get_entries_by_index(TupleElements.ADDRESS)(tuples,addr)

def get_failed_reads(tuples, returnkind: ListReturnKind):

    codesWith4 = get_entries_by_code(tuples,"^4")
    codesWith5 = get_entries_by_code(tuples,"^5")

    if(returnkind==ListReturnKind.COMBINED):
        return codesWith4.append(codesWith5)
    else:
        return codesWith4,codesWith5

def get_entries_by_extension(tuples, extension):
    return get_entries_by_index(TupleElements.FILEPATH)(tuples,"."+extension+"$")

#print(get_entries_by_code(read_log(),"200"))

#print(get_failed_reads(read_log(), ListReturnKind.COMBINED))

#print(get_entries_by_extension(read_log(), "jpg"))

def printEntries(tuples):
    for tuple in tuples:
        writeToStandardOutput(tuple)

if __name__=="__main__":
    printEntries(get_entries_by_extension(read_log(),"jpg"))