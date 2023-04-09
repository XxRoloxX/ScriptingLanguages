from pathlib import Path 
ARCHIVE_EXTENSION="tar.gz"


def validateArchive(pathToArchive):
    #extension = pathToArchive.split(".")[-2]+pathToArchive.split(".")[-1]
    #print(extension)
    if(not isFile(pathToArchive) or pathToArchive.split(".")[-2]+"."+pathToArchive.split(".")[-1]!=ARCHIVE_EXTENSION):
        raise Exception("Incorrect archive filepath! "+pathToArchive)
    
def isDirectory(pathToDirectory):
    pathObj = Path(pathToDirectory)
    return pathObj.is_dir()

def isFile(pathToFile):
    pathObj = Path(pathToFile)
    return pathObj.is_file()

def isValidPath(path):
    return Path(path).exists()

def validatePathAsDirectory(pathToDirectory):
    if not isDirectory(pathToDirectory):
        raise Exception("Path is not directory! " + pathToDirectory)
def validatePathExists(pathToFile):
    if not isValidPath(pathToFile):
        raise Exception("Path does not exist! " + str(pathToFile))