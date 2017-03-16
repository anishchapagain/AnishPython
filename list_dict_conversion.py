"""
Dictionaries {} - Conversion Lists from Dict and Dict from Lists
"""

d = {"Nepal":"Kathmandu","China":"Beijing","Japan":"Tokyo","Russia":"Moscow","Change":"Change"}

#Lists from Dictionary. items():tuple
print("\nDict : ",d)
countries = list(d.items())
print("List Countries - tuple : ",countries)
print("List Countries - dict : ",dict(countries))  #1st way

country = list(d.values())
print("List Country : ",country)
capital = list(d.keys())
print("List Capital : ",capital)

#Turn Lists into Dictionaries: zip()
print("\n Lists into Dictionaries zip()")
nations = list(zip(country,capital)) #list nations with tuple(country,capital)
print("Nations List: ", nations)
nation = dict(nations) #2nd way
print("Nation Dict: ", nation)

print(sorted(nation))#sorts by Key only
print(sorted(nation.values()))#sorts by Values only

#combining
#x = dict(list(dict.items())) 
#x = dict(list(zip(listkey,listvalue)))