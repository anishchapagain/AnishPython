"""
Logical , Comparison, identity and Membership Operators

Logical 'and': any one False is False!
True True = True
True False = False
False True = False
False False = False

Logical 'or': any one True is True!
True True = True
True False = True
False True = True
False False = False
"""

x=100
y=80

#Logical and
if x>0 and y<100:
        print (" x and y") #True
else:
        print(" x and y : fails") #False

#Logical or
if x>3 or y<10:
        print(" x or y")
else:
        print(" x or y : fails")

if x==100:
        print("Exactly 100")

#assign: =
#Condition
#Comparison Operators: Boolean TRUE/FALSE (Yes/No)

print('\n IF x==y : ',x==y)#double equal (is equal) maximum!
print(' IF x!=y : ',x!=y)#is not equal

print(' IF x>y : ',x>y)#greater
print(' IF x<y : ',x<y)#less

print(' IF x>=y : ',x>=y)#greater than and equal (>, ==) >=
print(' IF x<=y : ',x<=y)#less than and equal (<, ==) <=


#\n: newlines
#\t: tab


#Identity: is , is not
a=True
b = True
print("\n a is b : ", (a is b)) # ==  a==b
print("\n a is not b : ", (a is not b)) # !=  a!=b

#Membership: in, not in #CHECKing/Questioning
word = "Python"
print("\n 'P' in Python : ",('P' in word))
print("\n 'A' not in Python : ",('A' not in word)) #check if 'A' is not inside word 

