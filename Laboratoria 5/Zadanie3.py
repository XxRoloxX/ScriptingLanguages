from parsingUtils import *
from logUtils import *




def getFunctionForFormatedNumberOfBytes():
    sumOfBytes =[0]

    def getFormatedNumberOfBytesInner(line):
        sumOfBytes[0]+=len(line)
        return "Read "+str(sumOfBytes[0])+" bytes so far"

    return getFormatedNumberOfBytesInner


if __name__=="__main__":
    openFile("SSH/SSH.log",   [
                               textToNamedTupleAdapter(defaultLoggingDecorator(lambda ntLog: ntLog.message,logging.DEBUG)),
                               defaultLoggingDecorator(getFunctionForFormatedNumberOfBytes(),logging.DEBUG)
                               ])
