
def make_generator(f):
    def generator():
        currentValue=0
        index=0
        while True:
            yield f(currentValue),index
            currentValue+=1
            index+=1

    return generator

def fibonacciRecursive(elementIndex):

    def innerFibbonaci(previousElement, currentElement,currentIndex):
        if currentIndex<elementIndex:
            return innerFibbonaci(currentElement,currentElement+previousElement,currentIndex+1)
        else:
            return previousElement
        
    return innerFibbonaci(0,1,0)

def fibonacci(elementIndex):
    previousElement = 0
    currentElement = 1

    for i in range(0, elementIndex):
        previousElement,currentElement = currentElement,previousElement+currentElement


    return previousElement

def testGenerator(function, limit, debugFunction):
    generator = make_generator(function)
    for x,i in generator():
        if(i<=limit):
            debugFunction(x)
        else:
            break





if __name__ == "__main__":
    print("a)")
    testGenerator(fibonacci,10,print)
    print("b)")
    testGenerator(lambda x: x**2, 10,print)


