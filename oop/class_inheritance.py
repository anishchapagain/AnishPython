"""
Class: inheritance : Framework development (Python:module,  PHP- Zend, Wordpress, Magento...)
Abstraction
"""

class Parent:       # define parent, base class, super call
   parentAttr = 'P:100'
   _xyz=10
   __car="KIA"
   
   def __init__(self):
      print("Calling Parent constructor")
      
   def parentMethod(self):
      print('Calling Parent method')


      
class Child(Parent): # define child, derived class
   childPublic="C:200"
   _abc='Python' 
   _jeep="KIA-AT"  #mugling: 
   
   def __init__(self):
      print("Calling Child constructor")
      
   def childMethod(self):
      print('Calling Child method')
      super().parentMethod() #concept
      print(super()._xyz) #concept
      
      

c = Child() 
print(c.childMethod())
print(c.parentAttr)


"""
print(c._xyz)
print(c._abc)
print(Child._Child__jeep)
"""



"""
 def setAttr(self, attr):
      self.parentAttr = attr 
      
   def getAttr(self):
      print("Parent attribute :", self.parentAttr)

   def setName(self, arg):
      self.name = arg 
      
   def getName(self):
      print("Parent attribute :", self.name)
      
   @staticmethod
   def parentStatic():
      print("Parent Static")
   @classmethod
   def parentClass(cls):#self
      print("Parent ClassMethod")
   def abstractType(self):
      #print("I'm Abstract Implement me...")
      pass

      ===

   @staticmethod
   def childStatic(x):#self: error
      print("Child Static ",x)
   @classmethod
   def childClass(cls):#self
      print("Child ClassMethod")
   def abstractType(self):
      print("Calling Parent abstractType()")
      super().parentMethod()
      super().abstractType()



c = Child()  # instance of child
print(c._xyz)
print(c.parentAttr)
print(c._abc)
print(Child._Child__jeep) #Using Child access private attribute ...
#print(c.__jeep)
#print(c.__car)



#c.childMethod()      # child calls its method
#c.parentMethod()     # calls parent's method

#c.setAttr(200)       # again call parent's method
#c.getAttr()
# again call parent's method

c.abstractType()
c.childStatic(10)
c.childClass()

c.parentStatic()
c.parentClass()


p=Parent()

Parent.parentClass()

p.abstractType()
p.parentClass()
p.parentStatic()
"""

