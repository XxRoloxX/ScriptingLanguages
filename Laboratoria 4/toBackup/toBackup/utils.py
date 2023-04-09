import datetime

def createTimestamp():
    time:datetime = datetime.datetime.now()
    return time.strftime("%Y-%m-%d-%H-%M-%S")

def converToInt(value):
    try:
        return int(value)
    except Exception:
        return value