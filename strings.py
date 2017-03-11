"""
String variable and some basic operations
"""

words = "I Love Python"
x = 20
y = 30.80
print("Varaibles X is ", x," and Y is ",y)
print("Total x+y: ",x+y)
print("\nType of X and Y")
print("Type(x) :",type(x))
print("Type(y) :",type(y))

print("Type(words) : ",type(words))

print("Length words : ",len(words))#Total Length of Characters
print("Count words : ",words.count(' '))#spaces

print("UpperCase words : ",words.upper())
print("LowerCase words : ",words.lower())

print("Split words : ",words.split())#List