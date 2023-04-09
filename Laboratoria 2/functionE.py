from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper




def FunctionE():

    def functionE(requestLine):
      
        requestParameters = (parseRequest(validateRequest(requestLine)))
        
        status = getStatus(requestParameters)

        if(status=="200"):  
            return(requestLine)


    #functionWrapper(functionE)
    return functionE


    
if __name__ == '__main__':
    #FunctionE()
    functionWrapper(FunctionE())