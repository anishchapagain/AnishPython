"""
Functions: Recursive
"""

def factorial(n):
    print("Processing 'n' for Factorial : ", n)
    
    if n == 1:
        return 1
    else:
        # res = n * factorial(n-1)
        #print("Processing >> ", n, " factorial(",n-1,"):" ,res)
        
        return n * factorial(n-1)
        # return res	

print(factorial(5))