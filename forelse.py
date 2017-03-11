# FOR with IF-Else, break, continue

words = "I love Python"
print("Words: ", words)

print("For Loop 1.")
for char in words:
        if char=='P':
                print("P found ", char)
        else:
                print(" Else >> ",char)
else:
        print("Completed For 1.")

#quit()

print("For Loop 2.")
for char in words:
        if char =='P':
                print("P Found ", char)
        else:
                print(char)
        break #terminate current executing Block
else:
        print("Completed For")

print("Outside For 2.")

#quit()

print("For Loop 3.")
for char in words:
    if char == 'P' :
            print("P Found " , char) 
    else:
            print(char)
            continue #continue the main block
else:
        print("Completed For")

print("Outside For 3.")