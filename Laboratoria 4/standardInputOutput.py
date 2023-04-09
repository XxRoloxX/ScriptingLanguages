import sys
from os import environ

def writeToStandardOutput(result):
    sys.stdout.write(result)

def writeToErrorOutput(result):
    sys.stderr.write(result)

def readFromStandardInput():
    return sys.stdin.read()

def getEnvironmentVariable(variableName):
   return environ.get(variableName,False)

def getEnvironmentVariables():
   return [(key,environ[key]) for key in environ.keys()]

def getStandardInputArguments():
   if(len(sys.argv)>1):
    return sys.argv[1:]
   else:
      return []
   
def getArguments():
   if(len(sys.argv)>1):
      return sys.argv[1:]
   else:
      return []

def formatDictionaryToPrint(dictionary:dict):
   result=""
   for key,value in dictionary.items():
      result+=str(key)+": "+str(value)+"\n"
   return result
      
