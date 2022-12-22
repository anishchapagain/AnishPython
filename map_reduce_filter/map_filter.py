#map(): pandas->apply() , filter()
#z = list(zip(y,x))

#Map : apply a function to every element in a sequence, producing a new sequence
#map: 0 index: function to apply, all remaining are parameters!
#Map: results in True/False , apply: filter()

#Input: sample 100 -> filter() -> output: <100

#pos = list(map(lambda x:x>0, [1,-5,0,6,-2,8]))
#[True, False, False, True, False, True]
#positive = list(filter(lambda x:x>1, [1,-5,0,6,-2,8])) #comparison, select (10:(10-x))
#[1, 6, 8]
#reduce:map(10)->filter(<10)->reduce(1)


i = (str(i) for i in range(10)) #1
print(list(i))
print([str(i) for i in range(10)])

#Map: map(functionName,whereToApply) #multiple elements
i = map(str,range(10)) #2
print(list(i))

print(list(map(str,range(15))))

def sq(x): # 0 1 2 3 4 5 6 ..9
    #if x % 2==0:
    return x**2 #1, 5, 10......
#print(list(map(sq,range(10))))

def test(x):
    return x*5

#lambda x,y:x*y
 
ans=[]
for x in range(10):
    ans.append(sq(x))
print(ans)

fruit = ['apple','grape','banana','mango','orange']
size = ['tiny','small','medium','large']
drinks = ['cider','wine','juice','lassy','TEST']
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
#print("\n\n filter()")
positives = filter(lambda x:x>1, [1,-5,0,6,-2,8])
print(list(positives))
positives = map(lambda x:x*5, [1,-5,0,6,-2,8])
print(list(positives))

#Special Case: None
# If None is passed as 1st argument to filter(), it will remove elements which evaluate to False/Empty
true_elements = filter(None,[0,1,False,True,[],[1,2,3],'','python','Null',-1,-9])
print(list(true_elements))

#true_elements = filter(NULL,[0,1,False,True,[],[1,2,3],'','python','Null',-1,-9])
#print(list(true_elements))
#reduce

#True: 1 , False: 0
