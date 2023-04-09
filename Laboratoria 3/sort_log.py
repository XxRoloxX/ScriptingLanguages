from read_log import *
from parseTuples import *


def compareByElement(elementOfTupleToCompare: TupleElements):
    def getIndexedElement(tuple):
        validateTuple(tuple)
        return tuple[elementOfTupleToCompare.value]
    return getIndexedElement



def sort_log(tuples, elementOfTupleToCompare: TupleElements):
    if len(tuples)>0 and elementOfTupleToCompare.value<len(tuples[0]):
        return sorted(tuples, key=compareByElement(elementOfTupleToCompare))
    else:
        raise Exception("Index not present in given tuple!")
    
if __name__=="__main__":
    print(sort_log(read_log(),TupleElements.TRANSFERSIZE))