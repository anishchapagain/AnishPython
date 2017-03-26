"""
Class: conceptualizing and declarations
"""
#Class Just Picking the concept
print("\n Class Just Picking the concept")


print("\n Example 1")
class Classname: pass  

print("\n Example 2")
class Classname:
    #Class Varaibles
    attribute1= 'attribute1 Here'
    attribute2 = 'attribute2 Here'
    attribute3 = 'attribute3 for Method'

    def __init__(self):
        print("Object is created")

    def methods(self,attribute=None):
        return self.attribute3+" >> "+str(attribute)

print("Classname : ",Classname)
print("Classname() : ",Classname())
print("Classname.attribute1 : ",Classname.attribute1)
Classname.attribute1="Value to Attribute1"
print("Classname.attribute1 : ",Classname.attribute1)
print("Classname.attribute2 : ",Classname.attribute2)
print("Classname.methods : ",Classname.methods)
print("Classname().methods() : ",Classname().methods())
print("Classname.methods('HI....') : ",Classname().methods('HI from Methods()'))

print("\nClassname Object Created")
obj = Classname();
print("obj.attribute1 : ",obj.attribute1)
print("obj.methods('') : ",obj.methods("methods"))
print("obj.attribute3 : ",obj.attribute3)