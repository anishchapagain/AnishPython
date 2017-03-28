"""
Exception Handling
"""

print("Basics of Try Catch and Finally in Python")

try:
    num = float(input('Enter number to divide with'))
    result = 100.0/num
    print("TRY, Result : ",result)
except:
    print("EXCEPT, invalid Value Entered")
finally:
    print("FINALLY, try catch is goinf to end")

print("Out from Try catch Block 1")

try:
    num = float(input('Enter number to divide with'))
    result = 100.0/num
    print("TRY, Result : ",result)
except ValueError:
    print("Valid value not entered")

#IOError, ZeroDivisionError

#a=10
#b=15
#assert b < a, "b has to be smaller than a"