"""
Tuples () : immutable List
tuple cannot be changed in any way once it has been created

Constant values!
"""
emptyTuple = () #[] {}
t = (1,2,3,4,56.7,34.6)

print("Tuple : ",t)
print("Tuple type() : ",type(t)) 
print("Tuple length : ",len(t)) 
print("Tuple[0] : ",t[0]) 
print("Tuple[5] : ",t[5]) 

#del(t)

#try assigning
t[0]=100 
#print(t) #Error: 'tuple' object does not support item assignment

#unpacking Tuples
tuple_a = ("JSON","23.45","Oreilly Publication")
print(tuple_a)

#syntax: unpacking
(book,price,publication) = tuple_a

print(book,"\n")
book=book+' '+'file'
print(book,"\n")
print(price)
print(float(price)*3)
price=float(price)*1.25
print(price)
print("\n")
print(publication)
print(tuple_a)
