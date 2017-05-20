varList = [12,34,67,89,0,1,2,3,4]

def normalFunction():
    result = []
    for var in varList:
        result.append(var)
    return result

#every generator is an Iterator, but not Vice Versa. Uses 'yield' keyword and return an Iterator
def generatorFunction():
    for x in varList:
        yield x+2        

print("Normal Function TEST")
value = normalFunction()
print(type(value))
print(value)

print("\n\nYield Generator Test")
print(type(generatorFunction()))
valuey = list(generatorFunction())
print(valuey)

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
print("Loop Now >> ")
for i in yieldtest():
    print(i)

print("\n\nYield Fibonacci")
#Fibonacci function
def fib():
    a, b = 1, 2
    while True:
        # This yield statement is where the execution leaves the function
        yield b
        # This is where the execution comes back into the function, it came back while preserving the state
        if(b>100):
            break
        a, b = b, a + b
        print(a," : ",b)

iterVar = fib()
print(tuple(iterVar))