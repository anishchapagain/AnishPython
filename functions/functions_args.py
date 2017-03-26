"""
Functions: tuple reference *
"""
print("\n Example")
#args
def function_ref(x, y, *args): #*args: references tuple
    print ("\n X=", x, "& Y=", y) 
    print ("Args parameters : ", args)
    print("len :",len(args))

    if(len(args)>0):
        total=0
        for i in args:
            total = total + i
        sum = total + x+ y 
    else:
        sum = x+y
    
    print ("Sum :", sum) 

function_ref(10,20)
print("\n Again >> ")
function_ref(10,20,1,2,3)


#**kwargs
def function_ref_kwargs(**kwargs):
    for key,value in kwargs.items():
        print("Key :",key," Value:",value)

function_ref_kwargs(nepal='kathmandu',china='beijing')


#**kwargs Again
def function_ref_kwargs_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

kwargs = {"arg3": 3, "arg2": "two"}
function_ref_kwargs_call(1, **kwargs)