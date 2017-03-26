"""
while Loop
"""
number=0
while number <= 10:    #performs the Loop until given condition is satisfied
    print("Number : ",number)
    if number%2==0:
       print("\tNumber ",number," is Even")
    else:
       print("\tNumber ",number," is ODD")
    number+=1


#Infinite Loop with while
print("\n Enter 'quit' to terminate the Loop")
condition = True
while condition: #true
    name = input("Enter your Name : ")
    if name=='quit':
        print("\n Loop is Ending now...");
        condition = False # can use 'break'
    else:
        print("Name Entered : ",name)

else: #While Else
    print("Completed While")