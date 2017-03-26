"""
Logical , Comparison, identity and Membership Operators

Logical 'and'
True True = True
True False = False
False True = False
False False = False

Logical 'or'
True True = True
True False = True
False True = True
False False = False
"""

x=10
y=8
#Logical and
if x>0 and y<10:
        print (" x and y")
else:
        print(" x and y : fails")

#Logical or
if x>0 or y<10:
        print(" x or y")
else:
        print(" x or y : fails")


#Comparison Operators
print('\n IF x==y : ',x==y)
print(' IF x!=y : ',x!=y)
print(' IF x>y : ',x>y)
print(' IF x<y : ',x<y)
print(' IF x>=y : ',x>=y)
print(' IF x<=y : ',x<=y)


#Identity: is , is not
a=True
b = True
print("\n a is b : ", (a is b))
print("\n a is not b : ", (a is not b))

#Membership: in, not in
word = "Python"
print("\n 'P' in Python : ",('P' in word))
print("\n 'A' not in Python : ",('A' not in word))

