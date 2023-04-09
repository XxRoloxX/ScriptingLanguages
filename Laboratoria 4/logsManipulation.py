from validation import *
from filesManipulation import *
import json
from standardInputOutput import *

LOGS_DATE_KEY = "Backup date"
LOGS_ARCHIVED_FILES_KEY="Files archvied"
LOGS_NEW_ARCHIVE_LOCATION_KEY="New archive location"
BACKUP_DIR_ENV = "BACKUPS_DIR"
HOME_PATH = "HOME"
DEFAULT_BACKUP_DIR=getEnvironmentVariable("HOME")+os.sep+".backups"
BACKUP_LOGS_FILENAME="backups.json"


def createArchiveCreationLogs(date, absolutePathOfArchivedFiles, pathOfNewArchive):

    return {
        LOGS_DATE_KEY: str(date),
        LOGS_ARCHIVED_FILES_KEY: str(absolutePathOfArchivedFiles),
        LOGS_NEW_ARCHIVE_LOCATION_KEY:  str(pathOfNewArchive)
    }

def addToBackupLogs(date, absolutePathOfArchivedFiles, pathOfNewArchive):

    backupFolder = getBackupDirectoryPath()
    logsPath = backupFolder+os.sep+BACKUP_LOGS_FILENAME
    currentLogs = list()

    if isFile(logsPath):
        with open(logsPath, "r") as file:
            dataRead = file.read()
            if(len(dataRead)>0):
                try:
                    currentLogs = json.loads(dataRead)
                except Exception:
                    writeToErrorOutput("Incorrect logs format")
                    


    currentLogs.insert(0,createArchiveCreationLogs(date,absolutePathOfArchivedFiles, pathOfNewArchive))

    with open(logsPath,"w") as file:
        file.write(json.dumps(currentLogs))

def getBackupLogFilepath():
    backupDirectory = getBackupDirectoryPath()
    return joinPath(backupDirectory,BACKUP_LOGS_FILENAME)

def getBackupDirectoryPath():

    bdir = getEnvironmentVariable(BACKUP_DIR_ENV)
    return bdir if bdir else DEFAULT_BACKUP_DIR

def getDirectoryToBackupPath():
    path = getArguments()
    return path[0]

def getLogs():
    backupLogFilepath = getBackupLogFilepath()
    if not isFile(backupLogFilepath):
        raise Exception("No logs file available!")
    
    with open(backupLogFilepath, "r") as logFile:
        logs = json.loads(logFile.read())
    
    return logs

def parseLogsJSON(logs):

    result=""

    for i in range(len(logs)):
        result+="Opcja "+str(i)+"\n"
        result+=formatDictionaryToPrint(logs[i])+"\n\n"

    return result

def getArchivePathFromLogs(archiveIndex):
    logs = getLogs()
    return logs[archiveIndex][LOGS_NEW_ARCHIVE_LOCATION_KEY].strip()

def showLogs():
    logs =getLogs()
    writeToStandardOutput(parseLogsJSON(logs))