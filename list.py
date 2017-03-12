"""
Sequential Data Types: Lists, Tuples
List in Python is an ordered group of items or elements, may contain various elements of different types.
-Mutable, Extendable
-accessible by index, slicing etc
ex: myList = []
"""

emptyList = []
mixedList = [1,2,3,4,56.7,34.6]
mixedList_0 = [1,2,3,4,56.7,34.6,"the",'python']

print("MixedList :",mixedList)
print("Type of MixedList :",type(mixedList))
print("Length of MixedList :",len(mixedList))
print("Max of List :",max(mixedList))
print("Min of List :",min(mixedList))

#quit()


#accessing by index
print("\nList[0] : ",mixedList[0])
print("List[5] : ",mixedList[5])
print("List[lastIndex] : ",mixedList[len(mixedList)-1])

#Loop List values with their index
index=0
for value in mixedList:
    print(" mixedList[",index,"] : ",value)
    index+=1


#nested Lists
nested=[['C','C++','Java','Python','????'],['CSV','JSON','XML','TXT','SQL',''],['Cricket','Football','Badminton','']]
print("\n Nested List : ",nested)
print("Length of Nested  : ",len(nested))
print("Length of Nested[0]  : ",len(nested[0]))
print("Length of Nested[1]  : ",len(nested[1]))
print("Length of Nested[2]  : ",len(nested[2]))

print("\n Accessing Nested List")
print("Nested[0] : ", nested[0])
print("Nested[2] : ", nested[2])
print("\nNested[0][3] : ",nested[0][3])
print("Nested[2][1] : ", nested[2][1])


#Updating List Value
print("\n Updating List values")
nested[0][4]='PHP'
print("Nested[0][4] : ", nested[0][4])
print("Nested[0] : ", nested[0])
nested[2][3]='Tennis'
print("Nested[2][3] : ", nested[2][3])
print("Nested[2] : ", nested[2])


#Removing List Value
print("\n Removing List values")
print("Nested[1] : ", nested[1])
del nested[1][5]
print("Nested[1] : ", nested[1])

print("Nested[2] : ", nested[2])
del nested[2]
#print("Nested[2] : ", nested[2]) #ERROR: list index out of range
print("Nested : ",nested)


#Concatenation
print("\n Nested : ",nested)
newlist = nested[0]+nested[1]
newlist_0 = nested[0][0]+nested[1][0]
print("newList : ",newlist)
print("element only newList_0 : ",newlist_0)


#Membership operator
if "PHP" in newlist: #not in
    print('"PHP" is in newlist')
else:
    print("Inside ELSE")