"""
Functions: define---call---reuse : lines of code block

for x in l:
	print('X',x)
	if type(x)==int or type(x)==float:
		answer.append(x)
	else:
		if len(x)>0:
			for xx in x:
				answer.append(xx)
				
"""

#Example 1
print("\n 1. Function Basic example")
def add():    
    """Function add(): calculates sum of variables""" #Docstring-Not Compulsory..but is good practice!
    x=14
    y=19
    #now taking total or sum!
    total = x+y 
    #printing total
    print("Total : ",total)

#print("Showing DOCString :", add.__doc__)
#print("Showing __name__ :", add.__name__)
add()


#Example 2
print("\n 2. Function with return")
def add_return():
    x=10
    y=10
    total = x+y
    return total

value = add_return()
print("Value from add_return() : ",value)#20
print(add_return())
print(value)

#print("Value from add_return() : %d" % value)#20
#print("Value from add_return() : ",value[1])#20
#print("Value from add_return() : ",value[2])#20

#input: x,y -> process->total->return total (output)


#Example 3
print("\n 3. Function with parameter , argument and return")
def add_param(x,y): #parameters x and y
    total = x+y
    return total

value = add_param(2,3) #x=10 #y=15
print(value)
#value = add_param(2,56) #dynamic 
#print("Value from add_param() : %d" % value) #25
#print("Value from add_return() : ",value)
#print(add_param(10,15))
#add_param(100,15)

#Input (argument) -> Processing (code) -> Output (return)
#Example 4
print("\n 4. Function with default parameter & return")
def add_param_default(a,b=0): #parameters x and y
    total = a+b
    #print(total)
    return total

value = add_param_default()  
#value = add_param_default(10)
#value = add_param_default(10,34)
print("Value from add_return() : ",value)


#Example 5
print("\n 5. Function with default parameter & return")
def multiply(x=1,y=1,z=1): #parameters x and y and z
    total = x*y*z
    return total

#value = multiply() #ans: 1
value = multiply(3)
#value = multiply(3,2)
#value = multiply(3,2,5)
print("Value from multiply() : ",value)




