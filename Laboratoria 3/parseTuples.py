from enum import Enum

class TupleElements(Enum):
    ADDRESS=0
    DATE=1
    MESSAGE=2
    FILEPATH=3
    PROTOCOL=4
    CODE=5
    TRANSFERSIZE=6

def validateTuple(tuple):
    if len(tuple)<7:
        raise Exception("Incorrect tuple")


def getTupleAddr(tuple):
    validateTuple(tuple)
    return tuple[TupleElements.ADDRESS.value]

def getTupleDate(tuple):
    validateTuple(tuple)    
    return tuple[TupleElements.DATE.value]

def getTupleMessage(tuple):
    validateTuple(tuple)
    return tuple[TupleElements.MESSAGE.value]

def getTupleFilepath(tuple):
    validateTuple(tuple)
    return tuple[TupleElements.FILEPATH.value]

def getTupleProtocol(tuple):
    validateTuple(tuple)
    return tuple[TupleElements.PROTOCOL.value]

def getTupleCode(tuple):
    validateTuple(tuple)
    return tuple[TupleElements.CODE.value]

def getTupleTransferSize(tuple):
    validateTuple(tuple)
    return tuple[TupleElements.TRANSFERSIZE.value]