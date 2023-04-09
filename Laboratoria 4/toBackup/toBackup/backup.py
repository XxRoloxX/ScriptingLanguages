import pprint
from standardInputOutput import *
from pathlib import Path
import subprocess
import datetime
import os
import json
from validation import *
from filesManipulation import *
from logsManipulation import *
from utils import *


def createArchiveName(pathToDirectory):
    return createTimestamp()+"-"+str(pathToDirectory.split(os.sep)[-1])+"."+ARCHIVE_EXTENSION


def createBackupsArchive(pathToDirectoryToArchive):
    archiveName = createArchiveName(pathToDirectoryToArchive)
    createArchive(pathToDirectoryToArchive, archiveName).wait()
    moveFiles(archiveName, getBackupDirectoryPath())
    addToBackupLogs(createTimestamp(), getAbsolutePath(pathToDirectoryToArchive), getAbsolutePath(joinPath(getBackupDirectoryPath(),archiveName)))



if __name__=="__main__":
    path  = getDirectoryToBackupPath()
    createBackupsArchive(path)
