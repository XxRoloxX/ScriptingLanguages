from parseRequestUtils import *
from standardInputOutputUtils import *
from functionWrapper import functionWrapper
from functionResult import functionResult




def FunctionD():

    typeComparison = dict() 

    def functionD(requestLine):
       
        requestParameters = (parseRequest(validateRequest(requestLine)))
        extension = getFileExtension(requestParameters)

        if(isImage(extension)):
            extension="image"
        else:
            extension="other"

        typeComparison[extension] = typeComparison.get(extension,0)+1

        allFiles = typeComparison["image"]+ typeComparison["other"]
        
        return("Percenage of images:  "+ str(100*round(typeComparison["image"]/allFiles,2))+"%")

    #functionWrapper(functionD)
    return functionD

if __name__ == '__main__':
    #FunctionD()
    #functionWrapper(FunctionD())
    functionResult(FunctionD())