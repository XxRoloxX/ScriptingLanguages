from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper
from functionResult import functionResult


def FunctionC():

    largestResource = ["",0] #Path and size

    def functionC(requestLine):
       
        requestParameters = (parseRequest(validateRequest(requestLine)))
        size = getSize(requestParameters)
        path = getPath(requestParameters)

        if(size>largestResource[1]):
            largestResource[1]=size
            largestResource[0]=path
        
        return("Largest request was: "+largestResource[0]+" and it was "+str(largestResource[1])+"B")

    #functionWrapper(functionC)
    return functionC

if __name__ == '__main__':
    #FunctionC()
    #functionWrapper(FunctionC())
    functionResult(FunctionC())