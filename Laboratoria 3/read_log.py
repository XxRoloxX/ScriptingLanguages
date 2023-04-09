from standardInputOutputUtils import *
from parseRequestUtils import *





def read_log():
    line = readLineFromFStandardInput()
    output=[]
    while(line):
        try:
            validateRequest(line)
            tuple = convertRequestParametersToTuple(parseRequest(line))
            output.append(tuple)
        except Exception as e:
            writeToErrorOutput(e)
        
        line = readLineFromFStandardInput()
    return output
