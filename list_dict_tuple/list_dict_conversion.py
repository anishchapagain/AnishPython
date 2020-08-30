"""
Dictionaries {} - Conversion Lists from Dict and Dict from Lists
zip(): ??
"""

d = {"Nepal":"Kathmandu","China":"Beijing","Japan":"Tokyo","Russia":"Moscow","Change":"Change"}
#keys(), values(), items()

#d = ["Nepal","Kathmandu"]


#Lists from Dictionary. items():tuple
print("\nDict : ",d)

#x='12'
#print(str(x))

#list()
countries = list(d.items())

print("\nList Countries - tuple : ",countries)
print("\nList Countries - dict : ",dict(countries))  #1st way

country = list(d.values())
print("\nList Country : ",country)
capital = list(d.keys())
print("\nList Capital : ",capital)

#Turn Lists into Dictionaries: zip()
print("\n Lists into Dictionaries zip()")
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
