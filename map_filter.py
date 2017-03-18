"""
map() , filter()
"""
#Map : apply a function to every element in a sequence, producing a new sequence


i = (str(i) for i in range(10))
print(list(i))
print([str(i) for i in range(10)])

i = map(str,range(10))
print(list(i))
print(list(map(str,range(10))))


fruit = ['apple','grape','banana','mango']
size = ['tiny','small','medium','large']
drinks = ['cider','wine','juice','lassy']
def combine(fruit,size,drink):
    return '{} {} {}'.format(fruit,size,drink)

print(list(map(combine,fruit,size,drinks)))

#Filter: apply a function to each element in a sequence, constructing a new sequence with the elements if function returns True
#using filter()
print("\n\n filter()")
positives = filter(lambda x:x>0, [1,-5,0,6,-2,8])
print(list(positives))

# If None is passed as 1st argument to filter(), it will remove elements which evaluate to False
true_elements = filter(None,[0,1,False,True,[],[1,2,3],'','python','Null'])
print(list(true_elements))