#https://realpython.com/blog/python/primer-on-python-decorators/
#Decorators allow you to make simple modifications to callable objects like functions, methods, or classes
#decorators wrap a function, modifying its behavior

#http://www.python-course.eu/python3_decorators.php

print("1------Functions inside Function : ")
#1
def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()   
f()

#2
def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32
    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" 
    return result
print(temperature(20))

print("\n2--------- Functions as Parameters : ")
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()      
f(g)


print("\n3 ----------Functions Returning Functions : ")
def f(x):
    print("in f")
    def g(y):
        print("\tin g with y: ",y, " and x :",x)
        return y + x + 5 
    return g

nf1 = f(10)
nf2 = f(5)
print(nf1(5))
print(nf2(50))


print("\n4:1-----------DECORATOR")
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        y = func(x) #NoneType when called with foo()
        if type(y) is int:
            print("Integer parameter : ",y)
        elif type(y) is str:
            print("String Parameter : ",y)
        elif y is None:
            print("None Parameter : ",y)
        print("After calling " + func.__name__)

    return function_wrapper

@our_decorator # foo = our_decorator(foo)
def foo(x):
    print("Hi, foo has been called with " + str(x)) 

@our_decorator    
def succ(y):
    return y*100

foo("Hi")
succ(50)

print("\n4:2-----------DECORATOR")
def my_decorator(some_function):
    print("Decorator Called.")
    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper
def just_some_function():
    print("Wheee!")

#1
just_some_function = my_decorator(just_some_function)
just_some_function()

print("\n4:3-----------DECORATOR")
def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

a = divide(2,10)
print(a)
a = divide(2,0)
print(a)
a = divide(10,5)
print(a)

"""chaining decorator 
@decorator1
@decorator2
def somefunction():
equivalent to:  somefunction = decorator1(decorator2(somefunction))
"""