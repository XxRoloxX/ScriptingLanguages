from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper
from functionA import FunctionA
from functionResult import functionResult


def FunctionA_B():

    def functionA_B(requestLine):
        result = fun(requestLine)
        return(showDictionaryResults("302", result))
    

    fun = FunctionA()
    #functionWrapper(functionA_B)
    return functionA_B


if __name__ == '__main__':
    #FunctionA_B()
    #functionWrapper(FunctionA_B())
    functionResult(FunctionA_B())