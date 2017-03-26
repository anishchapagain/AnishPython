"""
Functions
"""
#Example 1
print("\n 1. Function Basic example")
def add():
    """Function add(): calculates sum of variables""" #Docstring
    x=10
    y=10
    sum = x+y
    print(sum)

print("Showing DOCString :", add.__doc__)
add()


#Example 2
print("\n 2. Function with return")
def add_return():
    x=10
    y=10
    sum = x+y
    return sum

value = add_return()
print("Value from add_return() : %d" % value)#20


#Example 3
print("\n 3. Function with parameter and return")
def add_param(x,y): #parameters x and y
    sum = x+y
    return sum

#value = add_param(x,y) #x=10 #y=15
value = add_param(10,15)  
print("Value from add_param() : %d" % value) #25
#print(add_param(10,15))


#Example 4
print("\n 4. Function with default parameter & return")
def add_param_default(x,y=0): #parameters x and y
    sum = x+y
    return sum

value = add_param_default(10)  
print("Value from add_param_default() : %d" % value)#11


#Example 5
print("\n 5. Function with default parameter & return")
def add_param_default_1(x,y=0,z=1): #parameters x and y and z
    sum = x+y+z
    return sum

value = add_param_default_1()  
print("Value from add_param_default_1() : %d" % value)#11