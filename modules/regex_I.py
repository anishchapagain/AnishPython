"""
Python Regular Expressions: re
https://regexone.com/references/python
http://www.regular-expressions.info/python.html
https://developers.google.com/edu/python/regular-expressions
"""
import re
#Search & Compile with Pattern
text = 'abbaaabbabbaaaBaaab'
regex_pattern2 = r'(ab)'
count=0
for match in re.findall(regex_pattern2, text):
    if match:
        count +=1
print('Found ',regex_pattern2,' ',count,' times')


print(re.findall(regex_pattern2,text))
regPat = re.compile(regex_pattern2)
res1 = regPat.search(text)
print("'ab' group : ",res1.group())

for match in re.finditer(regex_pattern2, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))

address = "One of the Postal code of, London, E15 4AL"
regex_pattern1 = r"([A-Z0-9]{2,}\s[A-Z0-9]{2,}$)"
res = re.compile(regex_pattern1).search(address)
postcode = res.group(0)
print("Group :" ,res.group())
print("Postcode of London : ",postcode)

#Group Name
print("Searching TODAY")
today = "Today is 2017-03-24"
datematch = re.compile(r'((19|20)\d\d)')
for match in re.findall(datematch, today):
    print(match)

#Listing
match = re.findall(datematch, today)
print(match)

datematch = re.search(r'(?P<year>19|20\d\d)(?P<delimiter>[- /.])(?P<month>0[1-9]|1[012])\2(?P<day>0[1-9]|[12][0-9]|3[01])',today)
# datematch = re.search(r'((?:19|20)\d\d)(?P<delimiter>[- /.])(?P<month>0[1-9]|1[012])\2(?P<day>0[1-9]|[12][0-9]|3[01])',today)
print("Group 0/ALL: ",datematch.group(0))

print("Group Year: ",datematch.group('year'))
print("Group 1: ",datematch.group(1))
print("Group Delimiter: ",datematch.group('delimiter'))
print("Group 2: ",datematch.group(2))
print("Group Month: ",datematch.group('month'))
print("Group 3: ",datematch.group(3))
print("Group Day: ",datematch.group('day'))
print("Group 4: ",datematch.group(4))



#Group Start End SPAN
mo = re.search("([0-9]{5,})|([0-9]+)", "Customer number: 232454, Date: February 12, 2011")
print(mo.group()) #23254
print(mo.group(0)) #23
print(mo.span()) #(17,23)
print(mo.start()) #17
print(mo.end())  #23
print(mo.span()[0]) #17
print(mo.span()[1])  #23

#Arranging with Search
l = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

for i in l:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print(res.groups())
    print("Group >> ",res.group(0,1,2,3))
    print(len(res.group()))
    print(res.group(3) + " " + res.group(2) + " " + res.group(1))


s = ['airplane', 'base', 'ALLIGATOR', 'Broad' ]
print("Filter 'A' : ",list(filter((lambda x: re.match(r'A', x)),s)))
print("Filter 'L' : ",list(filter((lambda x: re.match(r'L', x)),s)))