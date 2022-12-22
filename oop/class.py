"""
Class
"""
#Declaring Class 
#@decorators: they are special function that can override function,
#is a processor that modifies a function


#Abstract: Car->attribute1,attribute2,.....attribute19,__magicmethods__1,.......__magicmethods__30,generalFunc1.......generalFunc8
#remove magic methods in manual Class!

#Words: First Letter Capital (Car, TestCar)
#TEST: Constant

class Car:  
    """CAR: A vehicle representaton"""

    #Attributes (variables)
    milage="16.00"
    name_outer="KIA-KIA"
    model='4Wd-XYZ'
    __korean_car="KIA"

        
    #Methods (function)
    #self: points to the object!

    
    #def __init__(self): #empty constructor #obj = Car()
       
    def __init__(self, name, build_year): #Constructor: #obj = Car("Kia","2012")
        self.name = name #Kia
        self.build_year = build_year #2012
        print("__init__ > Object created")
        
    def __del__(self): #Destructor
        print("Object Deleted")
    
    """ __model__, getMilage"""
    def __model__(self,model):
        print("Model is: ",model)
    
    def getMilage(self): #Method
        print("Milage is: ",self.milage)

    def setMilage(self,val):
        self.milage=val

    def property(self,*args):
        """......"""
        country=args[0]
        color=args[1]
        return self.name+ " built on "+self.build_year+" from "+country+ " , coloured: "+color+" >> milage is "+self.milage


    @classmethod #classmethod must have a reference to a class object as the first parameter
    def property_class(cls,*args):#cls for Car  #TEST: Parent, Child > child.property_class()
        country=args[0]
        color=args[1]
        return cls.name_outer+ " from "+country+ " , coloured: "+color+" >> milage is "+cls.milage


    @staticmethod #similar to classmethod but doesn't take any obligatory parameters (like a class method)
    def property_static(*args):    #TEST: Parent, Child > child.property_class()
        country=args[0]
        color=args[1]
        return "@StaticMethod from "+country+ " , coloured: "+color+" >> milage is "+Car.milage

   @staticmethod 
   def property_new():    
        return "@StaticMethod Property_New!"
    
    def carproperty(self,*args): #Abstract: is to be overloaded by Childs
        pass   





print("\nCar Object Created")

Car.property_class();


obj = Car("Kia_Storm","2012") #<<
#obj1 = Car("Kia_Picanto","2017")

#print("obj.milage : ",obj.milage)
#obj.getMilage()

#get->method->receive
#set->method->create

print("__korean_car : ",Car._Car__korean_car)
#print("__korean_car : ",Car.__korean_car)

#will not run obj.__korean_car or Car.__korean_car #Mangling
#print(obj.__korean_car)

'''
print("obj.property() : ",obj.property("Korea","Silver Grey"))
print("@classmethod Class: ",Car.property_class("Korea","Red"))
print("@classmethod : ",obj.property_class("Korea","Red"))
print("@staticmethod Class : ",Car.property_static("Korea","Red"))
print("@staticmethod : ",obj.property_static("Korea","Red"))
'''
print(obj.__dict__)
print("\n DICT \n")
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
