"""
While Loop
Disadvantage: infinite loop!
"""
#start, condition-boundary, manage!

l=list(range(10))
for number in l:
    if number%2==0:
       print("\tNumber ",number," is Even")
    else:
       print("\tNumber ",number," is ODD")

print("For ended!! ",number)

#----------
number=0
while number <= 10:    #performs the Loop until given condition is satisfied

    print("Number : ",number)
    
    if number%2==0:
       print("\tNumber ",number," is Even")
    else:
       print("\tNumber ",number," is ODD")
     
    number= number+1 #number+=1


print("While ended!! ",number)

#Infinite Loop with while
print("\n Enter 'quit' to terminate the Loop")
condition = True
attempt=1
while condition: #true
    print("Attempt No:",attempt)
    name = input("\tEnter your Name : ")
    if name=='quit':
        print("\n\t Loop is Ending now...");
        condition = False # can use 'break'
    else:
        print("\tName Entered : ",name)
    attempt+=1
    

else: #While Else
    print("Completed While")
