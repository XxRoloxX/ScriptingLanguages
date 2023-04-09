from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper




def FunctionF():

    def functionF(requestLine):
        
        requestParameters = (parseRequest(validateRequest(requestLine)))
        
        hour = int(getHourOfTimestamp(requestParameters))

        if(hour>22 or hour<6):
            return(requestLine)

    #functionWrapper(functionF)
    return functionF


if __name__ == '__main__':
    #FunctionF()
    functionWrapper(FunctionF())