from collections import Counter

str = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"
print("Length of String:", len(str))

bucket={}
strL = str.lower()
#print(strL)

print(str)
words = str.split()
#print(words)


for word in words:
    print(word+ " > ")
    if word in bucket:
        bucket[word] +=1
    else:
        bucket[word] =1
    

print("Count >> ")
print(words.count("the"))              

print(bucket)
print("Counter\n\n")
print(Counter(words))

quit()

#for item in bucket.items():
 #   print(item)

for item in bucket.items():
    a = item[0]
    b = item[1]
    print(a+" > ",b)

    #print(item.value)

Counter(str)