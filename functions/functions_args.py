"""
Functions: tuple reference *
"""

print("\n Example")
#args
def add(x, y, *args): #*args: references tuple, Multiple Arguments
    print ("\n X=", x, "& Y=", y) 
    print ("Args parameters : ", args)
    print("len :",len(args))

    if(len(args)>0):
        total=0#1 3 6
        for i in args:#1 2 3
            total = total + i
        ans = total + x+ y 
    else:
        ans = x+y
    
    print ("Sum :", ans) 

add(20,3)
#print("\n Again >> ")
add(10,20,1,2,3)
add(10,20,1,2,3,4,5,6,7,8,9,10)
add(10,20,1,2,3,4,5,6,7,8,9,10,10,20,1,2,3,4,5,6,7,8,9,10,10,20,1,2,3,4,5,6,7,8,9,10)


#uncommon: level 1
#**kwargs: key-worded arguments --> more than one multiple variable
def function_ref_kwargs(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print("Key :",key," Value:",value)

function_ref_kwargs(nepal='kathmandu',china='beijing')


#uncommon: level 2
#**kwargs Again
def function_ref_kwargs_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)


kwargs = {"arg4": 3, "arg5": "two"}
function_ref_kwargs_call(1, **kwargs)#function_ref_kwargs_call(1,arg3=3,arg2=two)
