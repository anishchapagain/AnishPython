"""
List [] : Some advance Operations
"""

emptyList = []
mixedList = [1,2,3,4,56.7,34.6]
sentence = "the cat sat on the mat and the cat was playing with rat on the mat"

print("List : ",mixedList)
print("List index() : ",mixedList.index(4)) #return lowest index of that object

#generating and counting
words = sentence.split() #splits with spaces, split('cat')- split using 'cat'
print("\nWords : ",words)
print("Count 'cat' : ",words.count('cat')) 

#index(): find the position of an element
print("\n Word index() : ",words.index("playing")) 
print("\n Word index() : ",words.index("cat",3)) 
print("\n Word index() : ",words.index("cat",3,10)) #index("element",start_looking_from,end_looking_till)


#insert element at given index
words.insert(4,'cat')
print("\nAfter Insert (cat at 4) :", words) 

#sorting
words.sort()
print("\nSorted : ",words)

#reverse
words.reverse()
print("\nReversed : ",words)

#append
mixedList.append("Python")
print("\n List append() : ",mixedList)

#remove
mixedList.remove("Python")
print("\n List remove() : ",mixedList)

#pop : remove and return last object
print("\n List : ",mixedList)
print("POP : ",mixedList.pop())#last object if no index is given
print("List: ",mixedList)
print("POP with index : ",mixedList.pop(0))#with index
print("List: ",mixedList)

#extend, appending more than one element
newList = [11,33,56]
print("\nExtended : ",mixedList.extend(newList))
print("List: ",mixedList)

tuple_t = (10,20,30,40,55,66,99)
mixedList.extend(tuple_t)
print("\n Extended with Tuple : ",mixedList)

#extend using '+'
list_a=[1,2,3,4,5]
list_b=[6,7,8,9,10]
print("Extend using '+' : ",list_a+list_b)