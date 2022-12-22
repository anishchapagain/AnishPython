"""
For Loop 
"""

sentence = "the cat sat on the mat with"# the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"

print("Sentence is: ",sentence)
print("Length of sentence:", len(sentence))
print("Number of Occurrences of 't': ", sentence.count('t')) #3
print("length of string: ",len(sentence))

count=0
for char in sentence: #foreach char inside sentence:
    #count = count+1   #1 2 3 4 5.....20
    print(count," > ",char)
    count = count+1

for index,char in enumerate(sentence): #{}
    print("Char {} is at position {}.".format(char,index))

for char in enumerate(sentence): 
    print("Char {} ".format(char))

#range(start, stop[, step]) 
print("\n Range range(startfrom,stopat,interval)")
for num in range(1,22,2):
    print(num)
    if num==5: #num is exactly equals to 5
        print("Range (5): ",num)
    else:
        if num%2==0: #num divided by 2: if remainder is 0
            print("Even : ",num)

for i in range(10):
    print("Range : ",i)

#xrange() used for very long ranges, Python 3 handles same with range()
for i in range(5000): #xrange(5000)
    if(i%100==0):
        print("xRange % 100 : ",i)
