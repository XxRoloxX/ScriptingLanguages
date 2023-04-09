from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper
from functionA import FunctionA
from functionResult import functionResult


def FunctionA_C():

    def functionA_C(requestLine):
        result = fun(requestLine)
        return(showDictionaryResults("404", result))
    

    fun = FunctionA()
    #functionWrapper(functionA_C)
    return functionA_C


if __name__ == '__main__':
    #FunctionA_C()
    #functionWrapper(FunctionA_C())
    functionResult(FunctionA_C())