"""
Functions: Recursive
"""
import sys

def factorial(n):
    print("Processing 'n' for Factorial : ", n)
    
    if n == 1:
        return 1
    else:
        # res = n * factorial(n-1)
        #print("Processing >> ", n, " factorial(",n-1,"):" ,res)
        
        return n * factorial(n-1)
        # return res	

#print(factorial(5))

#using as Script, which allows execution in shell
if __name__=="__main__":
    factorial(int(sys.argv[1]))
    print(sys.argv)