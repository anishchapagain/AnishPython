"""
Comprehensions: List/For/Dictionary
Comprehensions are a special notation for building up lists, dictionaries from other lists, dictionaries, modifying and filtering them in the process
"""
"""
squares = []
for num in range(10):
    squares.append(num**2)

print("Squares :",squares)
"""

#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("sum([x**2 for x in range(10)]) >> ",sum([x**2 for x in range(10)])) 
#sum(x**2 for x in range(20))

##Using Comprehension Technique
squares_comp = [x**2 for x in range(10)]
print("[x**2 for x in range(10)] >> ",squares_comp) 
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_comp = [x for x in range(10) if x % 2 == 0]
print("[x for x in range(10) if x % 2 == 0] >> ",even_comp) 
#[0, 2, 4, 6, 8]

cube_squares = [x**2 if x % 2 == 0 else x**3 for x in range(10)]
print("[x**2 if x % 2 == 0 else x**3 for x in range(10)] >> ",cube_squares)
print(cube_squares)
#[0, 1, 4, 27, 16, 125, 36, 343, 64, 729]

#Nested 
print("\n NESTED Comprehension")
print([[y*2 for y in range(x)] for x in range(2,10)])

#quit()


#enumerate: index and value !
l=list(range(1,100,4))
for key,value in enumerate(l):
	print(key," :: ",value)

	
##Dictionary
print("\nDict CUBES : ",{x: x**3 for x in range(10)})
print("Dict CUBES EVEN: ",{x: x**3 for x in range(10) if x**3 % 2 == 0})


#After Function: adding two Dict's
print("\nMerging Dict >> ");
dict_a = {"Nepal":"Kathmandu" ,"Japan":"Tokyo","s":"s"}
dict_b = {"China":"Beijing", "Russia":"Moscow"}

def merge_dicts(d1, d2):
    return {k: v for d in (d1, d2) for k, v in d.items()}

dict_ab = merge_dicts(dict_a , dict_b) 
print(dict_ab)

print("\n{k: v for d in (dict_a, dict_b) for k, v in d.items()} >> ",{k: v for d in (dict_a, dict_b) for k, v in d.items()})


#Sentences
print("\n SENTENCE")
sentence = "the cat sat on the mat and the cat was happy with rat on the mat"
#print([x.title() for x in sentence.split()])

sentence_words=sentence.split() #strip()
print("\n1: ",{word:sentence_words.count(word) for word in sentence_words})
#['the', 'cat', 'sat', 'on', 'the', 'mat', 'and', 'the', 'cat', 'was', 'happy', 'with', 'rat', 'on', 'the', 'mat']


#alternate logic: traditional#
words=sentence.split()
unique1=list(set(words))

print("\nWords: ",words)
print("\nUnique Words: ",unique1)

unique2=[]
bucket={} #Dictionary
for word in words:       #the,cat,....the
    if word in bucket:   
        bucket[word] += 1     #a=1  a+=1: a=a+1
    else:
        unique2.append(word)
        bucket[word] = 1  #the : 1
print("\n2: ",bucket)
print("\n3: ",unique2)
