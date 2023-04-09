from collections import namedtuple
from parsingUtils import *
from logUtils import *


def readLine(line):
    return convertLineToNamedtuple(line)



if __name__=="__main__":
    openFile("SSH/SSH.log",   [
                               printingDecorator(readLine),
                               printingDecorator(textToNamedTupleAdapter(getIpv4sFromLog)),
                               printingDecorator(textToNamedTupleAdapter(getUserFromLog)),
                               printingDecorator(textToNamedTupleAdapter(getMessageFromLog)),
                               ])
