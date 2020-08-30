"""
Functions: Recursive
"""
from functools import reduce
#print(reduce(lambda a,b: a if (a < b) else b, [47,11,42,102,13,10]))

l=[47,11,42,102,13,10]
def check(a,b):
    if a>b:
        return a
    else:
        return b
print(reduce(check,[47,11,42,102,13,10]))





'''

def factorial(n):
    print("Processing 'n' for Factorial : ", n)
    
    if n == 1:
        return 1
    else:
        return n * factorial(n-1) #120*factorial(1)


print(factorial(8))
print(factorial(4))


def addNumber():
    #to be done later!
    pass


#input()
    
#main(): program execute block!
#using as Script, which allows execution in shell
#command line: cmd
if __name__=="__main__": #excute codes
    print("Inside Main!")
    #print(sys.argv)#argument of values from command line!
    #print(factorial(int(sys.argv[1])))
    add()
    '''
