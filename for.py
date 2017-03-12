"""
For Loop
"""

sentence = "the cat sat on the mat with the"
# rat cat and rat were playing in the mat and the cat was happy with rat on the mat"

print("Sentence is: ",sentence)
print("Length of sentence:", len(sentence))
print("Number of Occurrences of 'cat': ", sentence.count('cat'))

count=0
for word in sentence:
    count+=1 # count = count+1
    print(count," > ",word)


#range(start, stop[, step]) 

print("\n Range range(startfrom,stopat,interval)")
for i in range(1,21,1):
    print("Range : ",i)

for i in range(10):
    print("Range : ",i)

#xrange() used for very long ranges, Python 3 handles same with range()
for i in range(5000): #xrange(5000)
    if(i%100==0):
        print("xRange % 100 : ",i)