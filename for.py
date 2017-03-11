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