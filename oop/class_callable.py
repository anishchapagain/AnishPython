class A:
    """Class A, displaying Arguments. Magic function/dunder method"""


    def __init__(self):
        print("An instance of A was initialized")
        
    
    def __call__(self, *args, **kwargs):
        print("Arguments are:", args,"and keyworded are:", kwargs)

    
#if "__name__"="__main__":      
print(A.__doc__)
x = A()
print(x.__class__)


    """



    x = A() #creating Object x


    print(x.__doc__)


    print("\nCalling the instance:")
    x(3, 4, x=11, y=10, z=20,a=34)


    print("Let's call it again:")
    x(3, 4, x=11, y=10)
    """
