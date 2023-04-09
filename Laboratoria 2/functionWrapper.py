from standardInputOutputUtils import *

def functionWrapper(functionX):

    lineRead = readLineFromFStandardInput()
    
    while(len(lineRead)>0):

        try:
            functionResult = functionX(lineRead)
            
            if(functionResult):
                writeToStandardOutput(functionResult)

        except Exception as e:
            writeToErrorOutput(e)

        lineRead=readLineFromFStandardInput()



