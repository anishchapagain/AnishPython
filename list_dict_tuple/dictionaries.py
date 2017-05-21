"""
Dictionaries {} - unordered lists, accessible via the key not by position as Lists.
Similar to Associative array of other languages.
dict_a = {key:value, key:value, key:value}
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = (1, 2, 3, 4, 56.7, 34.6)
countries = {}  # empty Dictionary
d = {"Nepal": "Kathmandu", "China": "Beijing",
     "Japan": "Tokyo", "Russia": "Moscow", "Change": "Change"}

print("Dictionary : ", d)
print("Type() : ", type(d))
print("Length : ", len(d))

print("\nDictionary ['Nepal'] : ", d['Nepal'])  # d[0]: throws error
print("Dictionary ['Russia'] : ", d['Russia'])
print("Dictionary get() : ", d.get('Russia'))  # similar to line above


keys = d.keys()
values = d.values()
print("\nKeys only :", keys)  # Lists of Keys
print("Values only :", values)  # Lists of Values

# Change value
d['Change'] = ''
print("\nDictionary ['Change'] : ", d['Change'])

# del: delete the key with the Values
del d['Change']
print("\nDictionary del : ", d)

# check if Key exists
if "Nepal" in d:  # not in
    print("Nepal capital is ", d['Nepal'])

# print all Key value from Dictionary
# for key in d.keys():
# for value in d.values():
for item in d.items():  # returns Tuple
    print(item[0], " >> ", item[1])


# Adding key,value
print("\n Dict : ", d)
d["Singapore"] = "Singapore City"
d["Country"] = "Capital"
print("Dict added : ", d)

# update: concat (same keys with values provided)
d.update({"UK": "London"})
d.update({"Country": "London-England"})
print("\nDict update() : ", d)


# pop(): removes given key with its value
d.pop("Country")
print("\nDict pop() : ", d)

# popitem(): removes and returns (key,value) pair as Tuple()
print("Popitem : ", d.popitem())
print("\nDict : ", d)

# copy(): copy and generate new Dictionary
dcopy = d.copy()
print("\nCopy copy() : ", dcopy)

# clear(): clear content of Dictionary, set to empty
print("\nClearing Copied Dict")
dcopy.clear()
print("Copy Dict : ", dcopy)

# quit()
