"""
For Loop
"""

sentence = "the cat sat on the mat with"# the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"
'''
print("Sentence is: ",sentence)
print("Length of sentence:", len(sentence))
print("Number of Occurrences of 'cat': ", sentence.count('t')) #3
'''


count=0
for char in sentence: #foreach char inside sentence:
    count = count+1   #1 2 3 4 5.....20
    print(count," > ",char)


#range(start, stop[, step]) 

print("\n Range range(startfrom,stopat,interval)")
for num in range(1,22,2):
    print("Range : ",num)
    
'''
for i in range(10):
    print("Range : ",i)

#xrange() used for very long ranges, Python 3 handles same with range()
for i in range(5000): #xrange(5000)
    if(i%100==0):
        print("xRange % 100 : ",i)
'''
