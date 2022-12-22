"""
Class: conceptualizing and declarations
Abstraction
Encapsulation - Class ready!
Inheritance - A, B , C: B(A) , B(A, C)
Polymorphism (more than one form) - Parent, Child! Overloading (attribute/method) 
"""
"""
#Class Just Picking the concept
print("\n Class Just Picking the concept")

#abstract method is there inside Class!

print("\n Example 1")
class Classname1: pass  

"""


print("\n Example 2")
class Person: #Natural 
    #Class Varaibles
    attribute1= 'attribute1 Here'
    attribute2 = 'attribute2 Here'
    attribute3 = 'attribute3 for Method'
    model='XYZ123'

    def __init__(self,name): #constructor: Object initialize!
        print("Object is created")
        #print("Object Name is: ",name,'and model is',self.model)

    def __del__(self): #destructor: Object delete/free !!
        pass #print("Object is deleted")

    def methods(self):  #,attribute=None):
        return self.attribute3  #+" >> "+str(attribute)

    @classmethod #method can be accessed using ClassName!
    def test(self):  
        print("Method testing...") 


obj1 = Person('NAME1')
print(obj1.model)
print(Person.model)


"""
val = obj1.methods()
print(val)
#obj1.test()
Person.test()

del obj1

"""





"""
    def __del__(self): #destructor: Object delete/free !!
        print("Object is deleted")

    @classmethod
    def methods(self):  #,attribute=None):
        return self.attribute3  #+" >> "+str(attribute)
    
    
obj1 = Classname('NAME1')
obj2 = Classname('NAME2')

#print(type(obj1))
#print(type(obj2))

#Module/Package!

print("Classname : ",Classname)

print("Classname.attribute1 : ",Classname.attribute1)
Classname.attribute1="Value to Attribute1"

print("Classname.attribute1 : ",Classname.attribute1)

print("Classname.attribute2 : ",Classname.attribute2)

print("Classname.methods : ",Classname.methods)
print("Classname().methods() : ",Classname.methods())

print("obj.methods('') : ",obj1.methods())

'''
print("\nClassname Object Created")
print("obj.attribute1 : ",obj.attribute1)
print("obj.methods('') : ",obj.methods("methods"))
print("obj.attribute3 : ",obj.attribute3)
'''
"""
