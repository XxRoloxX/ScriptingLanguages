from functools import reduce
import math


def acronym(wordList:list):
    return "".join(list(map(lambda word: word[0] if len(word)>0 else "",wordList)))

def median(numberList:list):

    def calcMedian(sortedNumberList):
        return sortedNumberList[math.floor(len(sortedNumberList)/2)] \
            if len(sortedNumberList)%2!=0 \
            else (sortedNumberList[math.floor(len(sortedNumberList)/2)-1]
                  + sortedNumberList[math.floor(len(sortedNumberList)/2)])/2



    return calcMedian(sorted(numberList))


def squareRoot(squaredNumber:float, precision:float):

    def nextStep(currentApprox:float):
        return max(currentApprox- (currentApprox**2)/(2*currentApprox),0)
    
    def stopCriteria(currentApprox:float):
        return  abs(currentApprox**2 - squaredNumber)<precision
    
    def innerSquareRoot(currentApprox: float):
        print(currentApprox)
        return currentApprox if stopCriteria(currentApprox) else innerSquareRoot(nextStep(currentApprox))
    
    return innerSquareRoot(squaredNumber)


def checkIfCharIsAnAlphabetCharacter(character):
    return character<="z" and character>="a" or character>="A" and character <="Z"

def checkIfCharIsNotPunctuation(character):
    return checkIfCharIsAnAlphabetCharacter(character) or character==" "


def addWordsToCharacters(accumulator, word):

    return {k: v.union({word}) if k in word else v for k,v in accumulator.items()}


def make_alpha_dict(text:str):
    setOfLetters = set(filter(checkIfCharIsAnAlphabetCharacter,[*text]))
    mapOfLetters = {k:set() for k in setOfLetters}
    words = text.split(" ")
    mapOfLettersWithSets = reduce(addWordsToCharacters,words,mapOfLetters)
    return {k: list(v) for k,v in mapOfLettersWithSets.items()}


def flatten(argList):
    match argList:
        case []: return []
        case [element,*rest]: return flatten(element)+flatten(rest)
        case element: return [element]
    

if __name__=="__main__":
    print(median([1,2,3,21,37,4,420,5,8,7]))
    print(median([1,1,19,2,3,4,4,5,1]))
    print(squareRoot(3, 0.1))
    print(acronym(["Zaklad","Ubezpieczen","Spolecznych"]))
    print(make_alpha_dict("on i ona"))
    print(flatten([1,[2,3],[[4,5],6]]))