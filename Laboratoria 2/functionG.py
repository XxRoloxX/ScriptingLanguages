from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper

def filterWeekDay(requestLine, dayParameter):
        requestParameters = (parseRequest(validateRequest(requestLine)))
        
        day = getDayOfWeek(requestParameters)

        if(day==dayParameter):
            return(requestLine)


def FunctionG():

    def functionG(requestLine):
       
        return filterWeekDay(requestLine,4)

    #functionWrapper(functionG)
    return functionG



if __name__ == '__main__':
    #FunctionG()
    functionWrapper(FunctionG())