from validation import *
import os
import subprocess



def joinPath(firstPath, secondPath):
    return firstPath+os.sep+secondPath

def getAbsolutePath(path):
    return str(Path(path).absolute())

def unpackArchive(pathToArchvive, pathToUnpack):
    validateArchive(pathToArchvive)

    commandArguments = ["tar", "-xvzf", pathToArchvive, "-C", pathToUnpack]
    return executeBinary(commandArguments)

def removeFile(pathToFile):
    validatePathExists(pathToFile)
    commandArguments = ["rm", "-r", pathToFile]
    return executeBinary(commandArguments)


def emptyDirectory(pathToDirectory):

    validatePathAsDirectory(pathToDirectory)
    pathObj = Path(pathToDirectory)
    listOfFiles = [str(file) for file in pathObj.iterdir()]

    for file in listOfFiles:
        removeFile(file).wait()
    
def moveFiles(pathFrom, pathTo):

    validatePathExists(pathFrom)

    if(not isValidPath(pathTo) or not isDirectory(pathTo)):
        os.makedirs(pathTo)

    commandLineArguments = ["mv", pathFrom, pathTo ]
    return executeBinary(commandLineArguments)

def createArchive(pathToDirectoryToArchive, archiveName):

    validatePathAsDirectory(pathToDirectoryToArchive)
    commandLineArguments = ["tar", "-czvf",archiveName ,pathToDirectoryToArchive]
    return executeBinary(commandLineArguments)

def unpackArchive(pathToArchvive, pathToUnpack):
    validateArchive(pathToArchvive)

    commandArguments = ["tar", "-xvzf", pathToArchvive, "-C", pathToUnpack]
    return executeBinary(commandArguments)

def removeFile(pathToFile):
    validatePathExists(pathToFile)
    commandArguments = ["rm", "-r", pathToFile]
    return executeBinary(commandArguments)


def emptyDirectory(pathToDirectory):

    validatePathAsDirectory(pathToDirectory)
    pathObj = Path(pathToDirectory)
    listOfFiles = [str(file) for file in pathObj.iterdir()]

    for file in listOfFiles:
        removeFile(file).wait()
    

    

def executeBinary(arguments):

    return subprocess.Popen(arguments, stdin = subprocess.PIPE, stdout=subprocess.PIPE)