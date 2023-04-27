from itertools import tee

def forall(pred, iterable):

    def innerForAll(pred, iterable):
        try:
            return False if not pred(next(iterable)) else forall(pred, iterable)
        except StopIteration:
            return True
        
    return innerForAll(pred, tee(iterable)[1])
    

def exists(pred, iterable):
    return not forall(lambda x: not pred(x),tee(iterable)[1])

def atleast(n, pred,iterable):

    def innerAtLeast(pred, iterable, sum):
        try:
            match sum>=n:
                case True: return True
                case False: return innerAtLeast(pred,iterable,sum+1) \
                    if pred(next(iterable))\
                    else innerAtLeast(pred,iterable,sum)
        except StopIteration:
            return False
        
    return innerAtLeast(pred, tee(iterable)[1],0)

def atmost(n, pred, iterable):
    return not atleast(n+1,pred, tee(iterable)[1])



if __name__=="__main__":
    numberList = []
    print(forall(lambda x: x%2==0, iter(numberList)))
    print(exists(lambda x: x%2==0, iter(numberList)))
    print(atleast(3,lambda x: x%2==0, iter(numberList)))
    print(atmost(3,lambda x: x%2==0, iter(numberList)))