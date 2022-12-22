#Array: Collection/container -> DataType Same! : String!
#Iterate: move on indexwise/element side..List,Tuple,Dict,Set
#(String can be use as Iterator!)
#Mutable: Index base -> update (List!)  (neg: Immutable! -> String)

varList = [12,34,67,89,0,1,2,3,4]
"""
def normalFunction():
    result = []
    for var in varList:
        result.append(var+2)
    return result

print("MainList: ",varList)

print("Normal Function TEST")
value = normalFunction()
print(type(value))
print(value)

#every generator is an Iterator, but not Vice Versa.
#Uses 'yield' keyword and return an Iterator
def generatorFunction():
    for x in varList:
        yield x+2 #14,36,...6

    #create: temp array
    #append to temp array
    #finally: return (temp array)



print("\n\nYield Generator Test")
print(type(generatorFunction()))
valuey = list(generatorFunction())
print(valuey)
"""

#there might be more than one yield
print("\n\nYield TEST")
def yieldtest():
    yield "python"
    yield 20
    yield 35.69
    yield ["cat","mat"]
    yield ("sat","rat","hat")

print(type(yieldtest))
print(type(yieldtest()))
check = yieldtest()

print("check :" ,check)
print("check-a1 :" ,list(check))


"""
TASK: DEBUG!
1.
2.
3.
print("check-a2 :" ,list(check))
print("check-a3 :" ,list(check))
print("check-a4 :" ,list(check))

print("Loop Now >> ")
for i in yieldtest():
    print(i)
print(list(check))

#Database: ID: primary key (unique for each row!)
print("\n\nYield Fibonacci")
#Fibonacci function #2 
def fib():
    a, b = 1, 2
    while True:
        # This yield statement is where the execution leaves the function
        yield b
        # This is where the execution comes back into the function, it came back while preserving the state
        if(b>100):
            break
        a, b = b, a + b #a,b=2,3
        print(a," : ",b)

iterVar = fib()
print(tuple(iterVar))
"""
