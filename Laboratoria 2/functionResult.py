from standardInputOutputUtils import *

def functionResult(functionX):

    lineRead = readLineFromFStandardInput()
    functionResult =""
    
    while(len(lineRead)>0 and lineRead!="\n"):

        try:
            functionResult = functionX(lineRead)

        except Exception as e:
            writeToErrorOutput(e)

        lineRead=readLineFromFStandardInput()

    writeToStandardOutput(functionResult)
