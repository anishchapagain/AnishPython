"""
Python Regular Expressions: re
https://regexone.com/references/python
http://www.regular-expressions.info/python.html
https://developers.google.com/edu/python/regular-expressions
"""
import re
# re.search(pattern,str,re.I|re.MULTILINE|re.M)

# #Findall
#cat = "A fat cat doesn't eat oat but a cat eats bats"
#catmatch = re.findall("[acboe]at",cat) # [a-zA-Z0-9] - range of possible characters
#print("Findall found total ",len(catmatch)," Matches >> ",catmatch)
# ['cat', 'eat', 'oat', 'cat', 'eat', 'bat']

#split
#catmatch = re.split(r"[acboe]at",cat)
#print("Regular Split : ",catmatch)
#catmatch = re.split(r"\W+",cat)  #\w - word characters, \W - non word Characters  (+ one/more , * zero/more)
#print("Regular Split \W+ : ", catmatch)

#Sub - Substitute
#replace = re.sub("[acboe]at",'Cat',cat)
#print("Substitute : ", replace)

#Findall expressions
sentences = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;"
print("\nSentence: ",sentences)

meta = re.findall(r'[A-Za-z]{2}',sentences) # 2 char 
print("\n[A-Za-z]{2} : ",meta)

meta = re.findall(r'[A-Za-z]{2}\s',sentences) #with spaces after 2 char
print("\nr[A-Za-z]{2}\s : ",meta)

meta = re.findall(r'[A-Za-z]{2}\s(\w+)',sentences) #word after 2char and space
print("\nr[A-Za-z]{2}\s(\w+) : ",meta)

meta = re.findall(r'\b[A-Za-z]{2}\s(\w+)',sentences)
print("\nr\b[A-Za-z]{2}\s(\w+) : ",meta)
# print("Findall Length : ",len(meta))

meta = re.findall(r'[A-Za-z]{2}\s(\w+)',sentences) #\w+ [a-zA-Z_0-9]
print("Results : ",meta)
print("Length : ",len(meta))