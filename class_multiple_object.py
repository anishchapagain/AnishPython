"""
Class Example: Multiple Objects
"""

class Kia:  
    """Kia: brands for a car representaton"""
    #Class Varaibles

    _country="Korea"
    __state="Busan, Korea"
    capitalCity="Seoul"
    _brandName="Kia" 
     
    def __init__(self, model, build_year,color):
        self.color = color
        self.build_year = build_year
        self.model = model
        print("__init__ > Object created")
    
    def __del__(self):
        print("")

    def property(self):
        #x="picanto soul sorento sportage"
        #print(x)
        # return self._brandName + " built on " +self.build_year+" , Country: "+self._country+ " , coloured: "+self.color+" features : "+self.model
        return Kia._brandName + " built on " +self.build_year+" , Country: "+Kia._country+ " , coloured: "+self.color+" features : "+self.model
 
print("\nCar Object Created")
picanto_AT = Kia("2012","Auto Gear","Silver");
picanto_MN = Kia("2011","Auto Gear","Red");
soul = Kia("2014","Gear 4WD","Black");
quit()

print(Kia._brandName)
print(Kia._country)
print(Kia.capitalCity)
#print(Kia.property())
# print(Kia.__state)

print(picanto_AT.property())#AT
print(picanto_MN.property())#MN
print(soul.property())#Soul

#Altering
# Kia._brandName="Honda"
# print(Kia._brandName)
# print(soul.property())#Soul