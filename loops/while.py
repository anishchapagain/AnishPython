"""
While Loop: unclosed or to be maintained!
For Loop: closed/finite
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
population=0 #start: minimum
while population <= 10:    #performs the Loop until given condition is satisfied
    print("population : ",population)
   
    if population%2==0:
       print("\tpopulation ",population," is Even")
    else:
       print("\tpopulation ",population," is ODD")
     
    population= population+1 #maintain logic       #number+=1


print("While ended!! ",population)

#Infinite Loop with while
print("\n Enter 'quit' to terminate the Loop")
condition = True  #start
attempt=1
while condition: #true  #condition: check
    print("Attempt No:",attempt)
    name = input("\tEnter your Name : ")

    if len(name)<=3:
        #break #maintain
        continue
    
    if name=='quit' or name=='close':
        print("\n\t Loop is Ending now...");
        #break
        condition = False #maintain    # can use 'break'
    else:
        print("\tName Entered : ",name)
    attempt+=1
    

#else: #While Else
print("Completed While")
