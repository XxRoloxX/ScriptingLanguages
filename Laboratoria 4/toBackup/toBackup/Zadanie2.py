from Zadanie1 import *
import os
from standardInputOutput import *
from pathlib import Path

def getPathVariable():
    #return filterEnvironmentVariables(getEnvironmentVariables,"^PATH$")
    #print(type (environ["PATH"]))
    return environ["PATH"]

def fragmentStringBasedOnPathSeparator(paths: str):
    return paths.split(os.pathsep)

def formatPath(paths: str):
    formatedVariables = "\n".join(el for el in fragmentStringBasedOnPathSeparator(paths))
    return formatedVariables+"\n"

def getAllFilesFromDir(path):
    
    listFile =  [str(filePath).split(os.sep)[-1] for filePath in Path(path).iterdir() if filePath.is_file()]
    return listFile

def printFormatedFiles(files):
    for file in files:
        writeToStandardOutput("\t"+file+"\n")


def printAllFilesFromPaths(pathArgument: str):
    pathElements = fragmentStringBasedOnPathSeparator(pathArgument)

    for path in pathElements:
        files = getAllFilesFromDir(path)
        writeToStandardOutput(path+"\n")
        printFormatedFiles(files)
    

def functionA():
    writeToStandardOutput(formatPath(getPathVariable()))

def functionB():
    printAllFilesFromPaths(getPathVariable())

if __name__=="__main__":
   functionB()