import sys
import os

def writeToErrorOutput(message):
    #os.system("clear")
    print(message, file=sys.stderr)

def readLineFromFStandardInput():
    
    line = sys.stdin.readline()
    while(line=="\n"):
        line = sys.stdin.readline()

    return line.rstrip()

def writeToStandardOutput(data):
    print(data, file=sys.stdout)


def showFunctionResult(message):
    print(message)

def showDictionaryResults(key,dictionary):

    return (key + ": "+str(dictionary.get(key,"0")))
