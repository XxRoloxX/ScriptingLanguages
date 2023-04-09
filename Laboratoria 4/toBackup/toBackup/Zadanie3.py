from standardInputOutput import *
import json
import os

def countElementsToDictionary(transformFunction):

    countDictionary = dict()

    def getElementsFromLine(iterableCollection):
        if(len(iterableCollection)>0):
            for element in transformFunction(iterableCollection):
                countDictionary[element] = countDictionary.get(element,0)+1
        return getMostPopularKey(countDictionary)

    return getElementsFromLine

def getWordsFromLine(line:str):
    return line.split(" ")

def getMostPopularKey(dictionary:dict):
    biggestValue=0
    biggestValueKey =""

    for key,value in dictionary.items():
        if(value>biggestValue):
            biggestValueKey = key
            biggestValue = value
    
    return [biggestValueKey,biggestValue]
def getAbsoluteFilePath(path:str):
    return os.path.abspath(path)



def getNumberOfRows():
    numberOfRows = [0]

    def getRow(line):
        if(len(line)>0):
            numberOfRows[0]+=1
        return numberOfRows[0]
    
    return getRow

def getNumberOfCharacters():
    numberOfCharacters = [0]

    def getCharacterNumber(line):
        numberOfCharacters[0]+=len(line)
        return numberOfCharacters[0]
    return getCharacterNumber

def getNumberOfWords():
    numberOfWords = [0]

    def getWordNumber(line:str):
        if(len(line)>0):
            numberOfWords[0]+=len(line.split(" "))
        return numberOfWords[0]
    return getWordNumber

def getFileAnalysisFunctions():
    functions = {
        "NumberOfCharacters":getNumberOfCharacters(),
        "NumberOfWords":getNumberOfWords(),
        "NumberOfRows":getNumberOfRows(),
        "MostPopularWord":countElementsToDictionary(getWordsFromLine),
        "MostPopularCharacter":countElementsToDictionary(lambda line: line)
    }
    return functions

def executeFunctionDictionary(functions:dict):
    for key,value in functions.items():
        functions[key] = value("")
    return functions

def openFile(path, callbacks:dict):
    with open(path, "r") as file:
        line = file.readline().strip()
        while(line!=""):
            for fun in callbacks.keys():
                callbacks[fun](line)
            line = file.readline().strip()


def fileAnalysis():
    path = readFromStandardInput().strip()
    functions = getFileAnalysisFunctions()
    openFile(path,functions)
    resultDict = (executeFunctionDictionary(functions))
    resultDict["AbsolutePath"] = getAbsoluteFilePath(path)
    return json.dumps(resultDict)


if __name__=="__main__":
    writeToStandardOutput(fileAnalysis())