from functools import cache
from Zadanie4 import make_generator,fibonacci, testGenerator
from time import time

def make_generator_mem(f):

    @cache
    def memoizedFunction(arg):
        return f(arg)
    
    return make_generator(memoizedFunction)

def executeGenerator(generator, n):
    for x,i in generator():
        if i>n:
            break




if __name__=="__main__":
    oldGenerator= make_generator(fibonacci)
    newGenerator = make_generator_mem(fibonacci)

    executeGenerator(oldGenerator,1000)
    executeGenerator(newGenerator,1000)

    oldGeneratorStartTime = time()
    executeGenerator(oldGenerator,1000)
    print("Old generator: execution time: "+str(time()-oldGeneratorStartTime))

    newGeneratorStartTime = time()
    executeGenerator(newGenerator,1000)
    print("New generator: execution time: "+str(time()-newGeneratorStartTime))




