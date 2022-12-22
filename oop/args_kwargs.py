"""
Class: callable __call__: call object as a function

Abstraction: Plan->components(attribute, method, access, decorator)
Encapsulation: selected components (Code: Wrapping)
Polymorphism: Multi-form (more than one way to use)
Inheritance: Code/Attributes/Methods-reuse (Share)
"""
def add(*args): #list (args)
    print(sum(args))
    print(args[0])
    print(args[-1])
    print("---")
    
add(1,2)
add(1,2,3,4,5)
add(1,2,3,4,5,6,7,8,9,10)

"""

def add(**kwargs): #keyworded-args (Dict)
    print(kwargs)
    l = list(kwargs.keys())
    for i in l:
        print("--",kwargs[i])
    print("---")

add(x=1,a=2)
add(x=1,y=2,a=3,p=4,c=5)
"""

#TASK Recursive: calculate factorial using function. (3! = 3*2*1)
