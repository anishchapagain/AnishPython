"""
map(), filter(), reduce() and lambda
"""
from functools import reduce

#reduce() : continually applies the function to the sequence and it returns a single value
# 
print(reduce(lambda x, y: x+y, range(1,10))) #2+3=5+4=9+5
print(reduce(lambda a,b: a if (a > b) else b, [47,11,42,102,13])) # 47 42 47 102 102 13 102

quit()

print("\n Example 1")
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print(list(map(lambda x,y:x+y, a,b))) #[18, 14, 14, 14]
print(list(map(lambda x,y,z:x+y+z, a,b,c))) #[17, 10, 19, 23]


print("\n Example 2")
def add(x):
    return int(x[0])+int(x[1]) #int() optional here all vars are int

print([(x,x*2) for x in range(1,11)])                #[(1,2),(2,4),(3,6),...,(10,20)]

print("\n using map() and add()")
print(list(map(add,[(x,x*2) for x in range(1,11)]))) #[3,6,9,....30]

print("\n using lambda and map()")
print(list(map(lambda x:x[0]+x[1],[(x,x*2) for x in range(1,11)]))) #[3,6,9,....30]
print(list(map(lambda x:(x[0]+x[1])%2==0,[(x,x*2) for x in range(1,11)]))) #[3,6,9,....30]

print("\n using filter(),lambda")
print(list(filter(lambda x:(x[0]+x[1]) %2==0,[(x,x*2) for x in range(1,11)]))) #[3,6,9,....30]
quit()