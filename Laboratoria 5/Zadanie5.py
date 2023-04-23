import argparse
from Zadanie3 import getFunctionForFormatedNumberOfBytes
from parsingUtils import *
from logUtils import *
from Zadanie2 import *
from Zadanie4 import *




def configure_parser(parser:argparse.ArgumentParser):
    #parser.add_argument("--filepath",required=True, help="Path to file with SSH logs")
    #parser.add_argument("--minLogLevel", required=False, help="Lowest log level")

    subparsers = parser.add_subparsers(help="Decide witch functions to add")
    parser.add_argument("--filepath",required=True, help="Path to file with SSH logs")
    parser.add_argument("--minLogLevel", required=False, choices=["DEBUG","INFO","WARNING","ERROR","CRITICAL"],help="Lowest log level")


    parser_ex2 = subparsers.add_parser("ex2", help="Choose functions from exercise 2")
    parser_ex2.add_argument("--ip", action="store_true", help="get_ipv4s_from_log()")
    parser_ex2.add_argument("--user", action="store_true",help="get_user_from_log()")
    parser_ex2.add_argument("--type", action="store_true",help="get_message_type()")



    parser_ex4 = subparsers.add_parser("ex4", help="Choose functions from exercise 4") 
    parser_ex4.add_argument("--random" , type=int,help="get n random logs")
    parser_ex4.add_argument("--allStats", action="store_true", help="get stats for all logs")
    parser_ex4.add_argument("--userStats",action="store_true", help="get stats for each user")
    parser_ex4.add_argument("--logging",action="store_true", help="get most often logging users")



if __name__=="__main__":
    parser = argparse.ArgumentParser(prog="LOG PARSER")

    configure_parser(parser)

    args = parser.parse_args()
    dArguments = vars(args)


    functionsToExecuteByLine = []
    functionToExecuteAfterwards=[]

    aggregationFunctions = {
        "groupUserLogs": textToNamedTupleAdapter(groupUsersLogs())
    }


    functionsToExecuteByLine +=aggregationFunctions.values()

    minLogLevel = vars(logging).get(dArguments.get("minLogLevel"))

    if minLogLevel==None:
        minLogLevel=DEFAULT_LOG_LEVEL
        
    
    #functionsToExecuteByLine +=getDefaultLoggingFunctions(minLogLevel)
    functionsToExecuteByLine.append(defaultLoggingDecorator(getFunctionForFormatedNumberOfBytes(),minLogLevel))
    functionsToExecuteByLine.append(textToNamedTupleAdapter(defaultLoggingDecorator(lambda ntLog: ntLog.message,minLogLevel)))
    

    if dArguments.get("ip"):
        functionsToExecuteByLine.append(textToNamedTupleAdapter(defaultLoggingDecorator(getIpv4sFromLog,minLogLevel,"   IP")))
    if dArguments.get("user"):
        functionsToExecuteByLine.append(textToNamedTupleAdapter(defaultLoggingDecorator(getUserFromLog,minLogLevel,"   USER")))
    if dArguments.get("type"):
        functionsToExecuteByLine.append(textToNamedTupleAdapter(defaultLoggingDecorator(getMessageFromLog,minLogLevel,"   TYPE")))    

    if dArguments.get("random") or dArguments.get("allStats") or dArguments.get("userStats") or dArguments.get("logging"):
        functionsToExecuteByLine.append(aggregationFunctions["groupUserLogs"])

    if dArguments.get("random"):
        functionToExecuteAfterwards.append(printingDecorator(getCallable(getRandomUserLogsFromDictionary,aggregationFunctions["groupUserLogs"](None), int(dArguments.get("random"))),"Random logs: "))
    if dArguments.get("allStats"):
        functionToExecuteAfterwards.append(printingDecorator(getCallable(getStatisticsFromAllLogs,aggregationFunctions["groupUserLogs"](None)),"Stats of session time for all logs: "))
    if dArguments.get("userStats"):
        functionToExecuteAfterwards.append(printingDecorator(getCallable(getStatisticsForEachUser,aggregationFunctions["groupUserLogs"](None)),"Stats of session time each user: "))
    if dArguments.get("logging"):
        functionToExecuteAfterwards.append(printingDecorator(getCallable(getUsersWithMostLoginAttempts,aggregationFunctions["groupUserLogs"](None)),"Most login attempts: "))
    
    
    
    openFile(args.filepath, functionsToExecuteByLine)

    for fun in functionToExecuteAfterwards:
        fun()
    
