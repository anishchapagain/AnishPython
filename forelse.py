# FOR else: demo
str = "I love Python"
##for char in str:
##        if char=='P':
##                print("P found ", char)
##        else:
##                print(" Else >> ",char)
##else:
##        print("Completed For")



#FOR 2
##for char in str:
##        if char=='P':
##                print("found ", char)
##        else:
##                print(char)
##        break
##else:
##        print("Completed For")
##
##print("outside")


#FOR 3
for char in str:
        if char=='P':
                print("found ", char)
        else:
                print(char)
        continue
else:
        print("Completed For")

print("outside")
