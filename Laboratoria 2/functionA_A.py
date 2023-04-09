from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper
from functionA import FunctionA
from functionResult import functionResult


def FunctionA_A():

    def functionA_A(requestLine):
        result = fun(requestLine)
        return(showDictionaryResults("200", result))
    

    fun = FunctionA()
    #functionWrapper(functionA_A)
    return functionA_A


if __name__ == '__main__':
    #FunctionA_A()
    #functionWrapper(FunctionA_A())
    functionResult(FunctionA_A())