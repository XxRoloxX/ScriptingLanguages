import re
from standardInputOutput import *



def filterEnvironmentVariables(environmentItems,regex):
   return [item for item in environmentItems if re.search(regex,item[0])]
      
#filteredVariables = filterEnvironmentVariables(getEnvironmentVariables(),"PAT")

#for var in filteredVariables:
#   print(var)


def tupleComparator(tuple):
   return tuple[0]

#def filterEnvironmetVariablesFromArguments():
#   
##   args = getStandardInputArguments()
#   regex=""

#   for arg in args:
#      regex+="|"+arg

#   if(len(regex)>1): 
#    regex=regex[1:]
   
   #print(regex)


#   variables = filterEnvironmentVariables(getEnvironmentVariables(),regex)
#   sortedVariables = sorted(variables, key=tupleComparator)

#   return sortedVariables



def formatEnvironmentVariables(environmentVariables):
   formatedVariables = "\n".join(str(el) for el in environmentVariables)
   return formatedVariables+"\n"
 
def filterEnvironmetVariables(args):

   regex=""

   for arg in args:
      regex+="|"+arg

   if(len(regex)>1): 
    regex=regex[1:]
   
   #print(regex)


   variables = filterEnvironmentVariables(getEnvironmentVariables(),regex)
   sortedVariables = sorted(variables, key=tupleComparator)

   return sortedVariables
  


if __name__=="__main__":
    #writeToStandardOutput(formatEnvironmentVariables(filterEnvironmetVariablesFromArguments()))
   writeToStandardOutput(formatEnvironmentVariables(filterEnvironmetVariables(getStandardInputArguments())))