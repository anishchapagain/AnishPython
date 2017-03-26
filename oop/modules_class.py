"""
Modules: Helps organize the Python code we develop and Using it with other Code
A Module can include classes, functions, variables etc
"""
import datetime
import sys
#print(sys.builtin_module_names)

from class_multiple_object import Kia
#from class_multiple_object import *
#import class_multiple_object as obj

#import class_multiple_object.Kia #package



#referencing Class Kia from class_multiple_object

print(dir(Kia))
print("\nCalling Module : ",Kia.__name__," >> ",Kia.__class__)
print("\nDoc : ",Kia.__doc__)

print(Kia._brandName)
print(Kia._country)
print(Kia.capitalCity)
#print(Kia.property())

picanto_AT = Kia("2012","Auto Gear","Silver")
picanto_MN = Kia("2011","Auto Gear","Red")
soul = Kia("2014","Gear 4WD","Black")

print(picanto_AT.property())#AT
print(picanto_MN.property())#MN
print(soul.property())#Soul


print(Kia._brandName.__repr__)
print(repr(Kia._brandName))

print(Kia._brandName.__str__)
print(str(Kia._brandName))

#repr: unambigious , str: readable
print("\n Datetime")
today = datetime.datetime.now()
print(str(today))
print(repr(today))