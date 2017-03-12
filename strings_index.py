"""
String variable and some basic operations with Index, slicing etc..
"""

words = "I Love Python"  #type 1
words_again ='I Love Python' #type 2
name = 'student' 

#Multi-Line String #type 3
words_multi_line= '''Python is a scientific
programming language and is very famous
among the Researchers globally'''

#String by index, always use index inside []
print("Length of Words in '"+words+"' is ",len(words))#beginning of words
print("words[0] : ",words[0])#beginning of words

print("words[len(words)-1] : ",words[len(words)-1])#end of words

print("words[0:10] :", words[0:10])#0 to 10 char, change index values and check!!
print("words[3:8] :", words[3:8])#0 to 10 char, change index values and check!!

#using negative index, 
print("words[-1:] :", words[-1:])#0 to 10 char, change index values and check!!
print("words[-3:-1] :", words[-3:-1])#0 to 10 char, change index values and check!!
print("words[:] :", words[:])#0 to 10 char, change index values and check!!
print("words[:5] :", words[:5])#0 to 10 char, change index values and check!!

#Printing Chars: every 2nd char of the String
print(words[::2]) 


#Loop: Strings with index
print("Printing String with Its Index:\n")

count=0
for char in words:
    print (count ," : ", char)
    count+=1