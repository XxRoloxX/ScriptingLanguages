import sys
from standardInputOutput import *
from backup import *


def getRestorationPathFromArguments():
    args = getArguments()
    return "." if len(args)==0 else args[0]

def getArchiveToRestoreChoice():

    logs = getLogs()
    showLogs()
    writeToStandardOutput(f"Enter archive index to restore <{0}-{len(logs)-1}>: ")
    index = input()
    
    index = converToInt(index)


    while(type(index)!=int or index<0 or index>=len(logs)):

        writeToStandardOutput("Incorrect index, type again: ")
        index =input()
        index = converToInt(index)

    return index

def restoreArchive(pathToArchive, restorationPath):
    emptyDirectory(restorationPath)
    unpackArchive(pathToArchive,restorationPath)



if __name__=="__main__":
    restorationPath = getRestorationPathFromArguments()
    index = getArchiveToRestoreChoice()
    archiveToUnpack = getArchivePathFromLogs(index)
    restoreArchive(archiveToUnpack,restorationPath)
    
