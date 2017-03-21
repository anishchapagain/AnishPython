"""
Modules: Helps organize the Python code we develop and Using it with other Code
A Module can include classes, functions, variables etc
"""

import class_multiple_object as obj

print(dir(obj))
print("\nCalling Module : ",obj.__name__," >> ",obj.__file__)
print("\nDoc : ",obj.__doc__)

print(obj.Kia._brandName)
print(obj.Kia._country)
print(obj.Kia.capitalCity)
#print(obj.Kia.property())

picanto_AT = obj.Kia("2012","Auto Gear","Silver")
picanto_MN = obj.Kia("2011","Auto Gear","Red")
soul = obj.Kia("2014","Gear 4WD","Black")

print(picanto_AT.property())#AT
print(picanto_MN.property())#MN
print(soul.property())#Soul