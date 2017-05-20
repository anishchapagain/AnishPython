"""
Python Regular Expressions: re
https://regexone.com/references/python
http://www.regular-expressions.info/python.html
https://developers.google.com/edu/python/regular-expressions
"""
import re
# Anchors: ^ begining of Line, $ end of line
# re.search(pattern,str,re.I|re.MULTILINE|re.M)

# #Findall
cat = "A fat cat doesn't eat oat but a cat eats bats"
catmatch = re.findall("[acboe]at",cat) # [a-zA-Z0-9] - range of possible characters
print("Findall found total ",len(catmatch)," Matches >> ",catmatch)
# ['cat', 'eat', 'oat', 'cat', 'eat', 'bat']

#split
catmatch = re.split(r"[acboe]at",cat)
print("Regular Split : ",catmatch)
catmatch = re.split(r"\W+",cat)  #\w - word characters, \W - non word Characters  (+ one/more , * zero/more)
print("Regular Split \W+ : ", catmatch)

#Sub - Substitute
replace = re.sub("[acboe]at",'Cat',cat)
print("Substitute : ", replace)

#Findall expressions
sentences = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;"
print("\nSentence: ",sentences)

meta = re.findall(r'\b[A-Za-z]{2}\s',sentences) # 2 char 
print("\n\b[A-Za-z]{2} : ",meta)

meta = re.findall(r'[A-Za-z]{2}',sentences) # 2 char 
print("\n1 [A-Za-z]{2} : ",meta)

meta = re.findall(r'[A-Za-z]{2}\s',sentences) #with spaces after 2 char
print("\n2 [A-Za-z]{2}\s : ",meta)

meta = re.findall(r'[A-Za-z]{2}\s(\w+)',sentences) #word after 2char and space
print("\n3 [A-Za-z]{2}\s(\w+) : ",meta)

meta = re.findall(r'\b[A-Za-z]{2}\s(\w+)',sentences)
print("\n4 \b[A-Za-z]{2}\s(\w+) : ",meta)
# print("Findall Length : ",len(meta))

meta = re.findall(r'[A-Za-z]{2}\s(\w+)',sentences) #\w+ [a-zA-Z_0-9]
print("\n5 [A-Za-z]{2}\s(\w+) : ",meta)
print("Length : ",len(meta))

#\b word boundary
sentence='''Before the first character0 in the string0, if the first character1 is a word characters2.
After the last character3 in the string1, if the last character4 is a word character5.
Between two characters6 in the string2, where one is a word character7 and the other is not a word character8
Also BETWEEN Any words \B works and now word Boundary'''
meta = re.findall(r'in\s?(\w+)',sentence)
print("\n6. Word Boundary: ",meta)
meta = re.findall(r'\bin\s?(\w+)',sentence)
print("7. Word Boundary: \\b : ",meta)

meta = re.findall(r'e{2}n\s*(\w+)',sentence,flags=re.IGNORECASE)
print("8. e{2}n\s*(\w+) : ",meta)

meta = re.findall(r'e{2}n\s*(\w+)',sentence) # two 
print("9. e{2}n\s*(\w+) : ",meta)

