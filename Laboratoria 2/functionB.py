from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper
from functionResult import functionResult


def FunctionB():

    resultSumGB=[0]

    def functionB(requestLine):
        
        requestParameters = (parseRequest(validateRequest(requestLine)))
            
        resultSumGB[0] += int(getSize(requestParameters))/1000000000
            
        return ("Summary of data sent: "+str(round(resultSumGB[0],2))+"GB")

    #functionWrapper(functionB)
    return functionB



if __name__ == '__main__':
    #FunctionB()
    #functionWrapper(FunctionB())
    functionResult(FunctionB())