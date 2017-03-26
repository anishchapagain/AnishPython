"""
List/Dict comprehension
"""

#converting casting Using ZIP
print("\n Converting/Casting & Merging using ZIP ")

dict_a = {"Nepal":"Kathmandu" ,"Japan":"Tokyo","m":"n"}
dict_b = {"China":"Beijing", "Russia":"Moscow",'x':'y'}

print("\nExample 1")
#keys
print(dict_a.keys())
print(list(dict_a.keys()))#casting
#values
print(dict_b.values())
print(list(dict_b.values()))#casting
#merging Kes and Values
print(list(zip(dict_a.keys(),dict_b.values())))
print(dict(list(zip(dict_a.keys(),dict_b.values()))))


print("\nExample 2")
dict_abc = list(zip(dict_a.keys(),dict_b.values()))
print("Dict ABC >> ",dict_abc)
key, value = zip(*dict_abc)
print("Dict ABC Key : ",key)
print("Dict ABC Value : ", value)

"""
tuple_a = ("JSON","23.45","Oreilly Publication")
(book,price,publication) = tuple_a
print(book)
print(price)
"""