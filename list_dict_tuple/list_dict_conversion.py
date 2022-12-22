"""
Dictionaries {} - Conversion Lists from Dict and Dict from Lists
zip(): ??
"""

d = {"Nepal":"Kathmandu","China":"Beijing","Japan":"Tokyo","Russia":"Moscow","India":"Delhi"}
#keys(), values(), items()

#d0 = ["Nepal","China"]
#d1 = ["Kathmandu","Beijing"]

#Lists from Dictionary. items():tuple
print("\nDict : ",d)

#x='12'
#print(str(x))

#list()
countries = list(d.items())
#for k,v in d.items():
print("\nList Countries - tuple : ",countries)
print("\nList Countries - dict : ",dict(countries))  #1st way

country = list(d.values())
print("\nList Capital : ",country)
capital = list(d.keys())
print("\nList Country : ",capital)

#Turn Lists into Dictionaries: zip()
print("\n Lists into Dictionaries zip()")

#zip(): combine 
nations = list(zip(country,capital)) #list nations with tuple(country,capital)
print("\nNations List: ", nations)
nation = dict(nations) #2nd way
print("\nNation Dict: ", nation)

#sorted: Default ASC..order
#Desc..order: sorted(list,reverse=True)
print(sorted(nation))#sorts by Key only
print(sorted(nation.values()))#sorts by Values only

#combining
#x = dict(list(dict.items())) 
#x = dict(list(zip(listkey,listvalue)))
'''
