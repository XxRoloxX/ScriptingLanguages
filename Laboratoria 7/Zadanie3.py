import math
import random


DEFAULT_CHARSET = {chr(k) for k in range(65,91) }\
    .union({chr(k) for k in range(97,123) })\
    .union({chr(k) for k in range(48,58) })

print(DEFAULT_CHARSET)


class PasswordGenerator:
    def __init__(self,length,count,charset=DEFAULT_CHARSET):
        self.length = length
        self.charset = list(set(charset))
        self.maxCount = count
        self.currentCount=0

    def __iter__(self):
        return self
    
    def __generatePassword(self):

        return "".join([self.charset[math.floor(random.random()*len(self.charset))]\
                         for _ in range(0, self.length)])
        

    
    def __next__(self):

        match self.currentCount<self.maxCount:
            case True:  self.currentCount+=1; return self.__generatePassword()
            case False: raise StopIteration
        

if __name__=="__main__":
    generator = PasswordGenerator(10,3)
    for i in generator:
        print(i)