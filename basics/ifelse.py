"""
Decision Making: If Elif Else
"""

#Input from Keyboard
age = int(input("Enter your age: "))     #Type casting String input to Int
print("Age :",age,"\nType of age:",type(age))

#If Block
if age <= 20:
        print("Age is < or = 20")                        
else:
        if age>20 and age<=30:  #TODO  
        #condition and condition == TRUE (both), condition or condition == any one condition can be true

                print("Age is > 20 and <= 30")
        elif age<60:        
                print("Age is > 30")
        else:
                print("Age is above 60")
        print("My Condition above didn't Matches")



age=35
#Ternary Expressions (value = true if condition else)
#if condition:
#        print
#else:
#        print

print("\n Ternary Expressions")
#print('age is ',age if age >=30 else 'Less than 30')
print("Yes!" if age >=30 else "NO!")
