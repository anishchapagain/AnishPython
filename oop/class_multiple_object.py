"""
Class Example: Multiple Objects
"""
class Kia:
    """
    """
    
class ATX324:
    
    """Kia: brands for a car representaton"""
    
    capitalCity="Seoul" #public    (inherit=Open)
    _country="Korea"    #protected (inherit=Partial)
    _brandName="Kia"    #protected (inherit=Partial)
    __year="2021"       #private (inherit=NO)
    __eng_model = "ATX-324 A" #private (inherit=NO)

     
    def __init__(self, model, build_year,color):
        self.color = color
        self.build_year = build_year
        self.model = model
        print("__init__ > Object created")

    
    def __del__(self):
        print("")


    def property(self):
        return Kia._brandName + " built on " +self.build_year+" , Country: "+Kia._country+ " , coloured: "+self.color+" features : "+self.model


class ATX326:
    
    def test(self):
        return Kia._brandName + " built on " +self.build_year+" , Country: "+Kia._country+ " , coloured: "+self.color+" features : "+self.model

    



#public: accessible to all (parent->child)
#protected: restricted property (parent->child) 







# print("\nCar Object Created")
picanto_AT = Kia("Auto Gear","2012","Silver")

print(picanto_AT.model)
#print(picanto_AT.property())











# picanto_MN = Kia("2011","Auto Gear","Red")
# soul = Kia("2014","Gear 4WD","Black")


# print(Kia._brandName)
# print(Kia._country)
# print(Kia.capitalCity)
# #print(Kia.property())
# # print(Kia.__state)

#print(soul.property())#Soul

# #Altering
# # Kia._brandName="Honda"
# # print(Kia._brandName)
# # print(soul.property())#Soul
