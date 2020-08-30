"""
map(): pandas->apply() , filter()
"""
#Map : apply a function to every element in a sequence, producing a new sequence
#map: 0 index: funciton to apply, all remaining are parameters!
#Map: results in True/False , apply: filter()

#Input: sample 100 -> filter() -> output: <100

i = (str(i) for i in range(10)) #1
print(list(i))
print([str(i) for i in range(10)])

#Map: map(functionName,whereToApply) #multiple elements
i = map(str,range(10)) #2
print(list(i))

print(list(map(str,range(15))))

def sq(x): # 0 1 2 3 4 5 6 ..9
    return x**2+1 #1, 5, 10......
print(list(map(sq,range(10))))

fruit = ['apple','grape','banana','mango']
size = ['tiny','small','medium','large']
drinks = ['cider','wine','juice','lassy']
def combine(fruit,size,drink):
    return '{} {} {}'.format(fruit,size,drink)

print(list(map(combine,fruit,size,drinks)))

def sq(x): # 0 1 2 3 4 5 6 ..9
    if x>0:
        return x
positives = filter(sq,[1,-5,0,6,-2,8])
print(list(positives))

#Filter: apply a function to each element in a sequence, constructing a new sequence with the
#elements if function returns True
#using filter()
print("\n\n filter()")
positives = filter(lambda x:x>0, [1,-5,0,6,-2,8])
print(list(positives))
#positives = filter(lambda x:x, [1,-5,0,6,-2,8])
#print(list(positives))

#Special Case: None
# If None is passed as 1st argument to filter(), it will remove elements which evaluate to False/Empty
true_elements = filter(None,[0,1,False,True,[],[1,2,3],'','python','Null',-1,-9])
print(list(true_elements))

#true_elements = filter(NULL,[0,1,False,True,[],[1,2,3],'','python','Null',-1,-9])
#print(list(true_elements))
#reduce

