import sys

def readFileFromStandardInput():
    result=""
    for line in sys.stdin:
        result+=line

    return result
