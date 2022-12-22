"""
For Loop: if else , break, continue, pass
pass : is the non-operational statement in Python.
Can be used in blocks where no action is to be taken.
"""

words = "I love Python"
print("Words: ", words)

print("\nFor Loop 1.")
for char in words:
        if char=='P':
                print("P found ", char)
        else:
                print(" Else >> ",char)        
else:
        print("For loop is completed now!")

print("\nFor Loop 2.")
for char in words:
        if char == 'P':
                print("P Found ", char)
                break
        else:
                print(char)

        #print("Before break")
        #break #terminate current executing Block
        #print("After break")
else:
        print("Completed For")

print("Outside For 2.")

print("\nFor Loop 3.")
for char in words:
    if char == 'P' :
            print("P Found " , char)                    
    else:
            print(char)
            #continue #continue the main block
else:
    print("Completed For")
print("Outside For 3.")

#using pass: only required as python uses whitespace to delimit blocks
print("\nFor Loop 4 with 'pass'.")
for char in words:
    if char == 'P' :
            pass
            #print("P Found " , char) 
    else:
            print(char)
else:
        print("Completed For")

print("Outside Loop 4 using 'pass'.")
