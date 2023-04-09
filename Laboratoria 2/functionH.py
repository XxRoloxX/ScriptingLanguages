from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper




def FunctionH():

    def functionH(requestLine):
        
        requestParameters = (parseRequest(validateRequest(requestLine)))
        
        domain = getHostDomain(requestParameters)

        if(domain=="pl"):
            return(requestLine)


    #functionWrapper(functionH)
    return functionH


if __name__ == '__main__':
    #FunctionH()
    functionWrapper(FunctionH())