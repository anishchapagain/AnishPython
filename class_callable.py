"""
Class: callable __call__
"""

class A:
    """Class A, displaying Arguments"""

    def __init__(self):
        print("An instance of A was initialized")
    
    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)
              
print(A.__doc__)
x = A() #creating Object x
print(x.__doc__)

print("\nCalling the instance:")
x(3, 4, x=11, y=10)

print("Let's call it again:")
x(3, 4, x=11, y=10)