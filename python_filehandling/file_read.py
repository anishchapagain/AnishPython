import os

fopen = open(os.getcwd()+"\python_filehandling\content.txt") #fopen('content.txt','r')
print(fopen.read())
fopen.close()
