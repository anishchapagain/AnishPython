"""
Class
"""
#Declaring Class 
#@decorators: they are special function that can override function,
#is a processor that modifies a function

class Car:  
    """CAR: A vehicle representaton"""
    milage="16.00"
    name_outer="KIA-KIA"
    __korean_car="KIA"

    def __init__(self, name, build_year):
        self.name = name #Kia
        self.build_year = build_year #2012
        print("__init__ > Object created")
    
    def __del__(self):
        print("Object Deleted")

    def property(self,*args):
        country=args[0]
        color=args[1]
        return self.name+ " built on "+self.build_year+" from "+country+ " , coloured: "+color+" >> milage is "+self.milage
 
    @classmethod #classmethod must have a reference to a class object as the first parameter
    def property_class(cls,*args):#cls for Car
        country=args[0]
        color=args[1]
        # return cls.name+ " built on "+cls.build_year+" from "+country+ " , coloured: "+color+" >> milage is "+cls.milage
        # return "@ClassMethod from "+country+ " , coloured: "+color+" >> milage is "+cls.milage
        return cls.name_outer+ " from "+country+ " , coloured: "+color+" >> milage is "+cls.milage


    @staticmethod #similar to classmethod but doesn't take any obligatory parameters (like a class method)
    def property_static(*args):
        country=args[0]
        color=args[1]
        # return Car.name_outer+ " from "+country+ " , coloured: "+color+" >> milage is "+Car.milage
        return "@StaticMethod from "+country+ " , coloured: "+color+" >> milage is "+Car.milage
        

print("\nCar Object Created")
obj = Car("Kia","2012");

print("obj.milage : ",obj.milage)
print("__korean_car : ",Car._Car__korean_car) #will not run obj.__korean_car or Car.__korean_car #Mangling
print("obj.property() : ",obj.property("Korea","Silver Grey"))
print("@classmethod : ",Car.property_class("Korea","Red"))
print("@staticmethod) : ",Car.property_static("Korea","Red"))
print(obj.__dict__)
print(Car.__dict__)


#@classmethod
# Like static methods class methods are not bound to instances, 
# but unlike static methods class methods are bound to a class. 
# The first parameter of a class method is a reference to a class, i.e. a class object. 
# They can be called via an instance or the class name

#@staticmethod
#don't have any access to what the class is- it's basically just a function, 
# called syntactically like a method, 
# but without access to the object and it's internals (fields and another methods), while classmethod does
#they are helpful in method overriding

#Abstract methods: @baseclass.abstractmethod eg: @Car.abstractmethod
#Is a method defined in Base class, without any implementation.
#Class inheriting Base class should override the abstract method to process.