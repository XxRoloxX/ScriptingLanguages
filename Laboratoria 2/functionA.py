from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper
import os




def FunctionA():
    resultDict = dict()

    def functionA(requestLine):
       
        requestParameters = (parseRequest(validateRequest(requestLine)))
        status = getStatus(requestParameters)
        resultDict[status]= resultDict.get(status,0)+1
    
        return resultDict

    return functionA

