from pathlib import Path
import pprint
import subprocess
from standardInputOutput import *
import json

FILE_ANALYSIS="./Zadanie3.py"

def walkThroughDir(path:Path, callback):

    pathObj = Path(path)
    #print(path)

    if(pathObj.is_dir()):

        for innerPath in pathObj.iterdir():
            walkThroughDir(innerPath,callback)

    elif(pathObj.is_file()):
        callback(path)

def sumFileData():

    readFiles = [dict(),0] #Sum dictionary, readFiles
    sumDictionary = readFiles[0]

    def sumFileDataInner(fileData: dict):

        if(len(fileData.keys())>0):

            for key,value in fileData.items():

                if type(value)==list:
                    sumDictionary[key] = (sumDictionary[key] if sumDictionary.get(key,["",0])[1]>value[1] else value)

                elif type(value)==int:
                    sumDictionary[key] = sumDictionary.get(key,0)+value

            readFiles[1]+=1

        return readFiles
    return sumFileDataInner

def runFileAnalizer(callback):

    def runFileAnalizerInner(path: Path):

        if(path.is_file()):

            process = subprocess.Popen(["python",FILE_ANALYSIS], stdin = subprocess.PIPE, stdout=subprocess.PIPE)

            process.stdin.write(bytes(str(path).strip(),"utf-8"))
            process.stdin.close()
            try:
                resultJson = json.loads((process.stdout.read()).decode("UTF-8"))
                callback(resultJson)
            except Exception:
                writeToErrorOutput("Not able to parse binary file: "+str(path))

           
            
    return runFileAnalizerInner


if __name__=="__main__":

    path  = readFromStandardInput().strip()
    summingFunction = sumFileData()
    walkThroughDir(path, runFileAnalizer(summingFunction))
    writeToStandardOutput("Read files: "+str(summingFunction({})[1])+"\n")
    writeToStandardOutput(formatDictionaryToPrint(summingFunction({})[0]))