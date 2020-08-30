"""
Exception Handling #Priority try-catch!
Error case: manage
"""

#basic code
num = float(input('Enter number to divide with'))
print("Num ",num)
result = 100.0/num
print("TRY, Result : ",result)

#Example: 1
print("Basics of Try Catch and Finally in Python")
try:
    num = float(input('Enter number to divide with'))
    result = 100.0/num
    print("TRY, Result : ",result)
except:
    print("Please check the entered value from Keyboard!")
finally:
    print("FINALLY, try catch is going to end")

print("Out from Try catch Block 1")

#Example: 2
try:
    num = int(input('Enter number to divide with'))
    result = 100.0/num
    print("TRY, Result : ",result)
except ValueError:
    print("Valid value not entered")
except ZeroDivisionError:
    print("ZeroDivisionError, pls check the input (Input should be greater than 0 and Interger)")
except SyntaxError:
    print("Check the Syntax!")
except AssertionError:
    print("Check the Syntax!")

    
#ValueError, TypeError, IOError, ZeroDivisionError

#a=10
#b=15
#assert b < a, "b has to be smaller than a"
