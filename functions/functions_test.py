"""
Function: create, call, use with examples
"""
#function define
def hello(fname,lname,age):
        """
        Accepts 3 parameter (fname:str,lname:str,age:int).
        Displays a greeting message if age>20.
        """
        if age>20:
                print("Hello ("+fname+" "+lname+ ") welcome to Python!")
        else:
                print("Not applicable because of ",age)
                
def sumMinMax(col):#define definition
        """
        ....
        """
        #col: parameter, argument
        print(col)
        print("Length of collection: ",len(col))
        print("Sum=",sum(col)," Min=",min(col)," Max=",max(col))


def add(x,y):
        total=x+y
        print(total)
        return total  #ideally: 1, last line

"""
ans = add(10,20) # ans = total = add(10,20)
x = add(0,2)
y = add(560,29)
z=50
print(y+z)
        
#function call
#sumMinMax(['a',1,45,'apple']) #col=[11,50]	
#sumMinMax([11,50]) #col=[11,50]	
#sumMinMax(list(range(11,50))) #col = list(range(11,50))
hello("Peter","XYZ",40)
hello("Santosh","YUC",19)
hello("Manish","YITOP",25)
hello("Raj","RRWWW",18)
hello("Aasira","qwrretr",45)
hello("Aasira","qfsdfsdfsdfr",22) # fname,lname,age
"""
