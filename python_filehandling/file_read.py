import os
print(os.getcwd())

print(os.curdir)
print(os.name)
print(os.uname)
print(os.path)
print(os.path.split())
print(os.mkdir('dirname'))
print(os.makedirs('/dirname1/dirname2'))
# print(os.removedirs())
print(os.rename())


fopen = open(os.getcwd()+"\python_filehandling\content.txt") #fopen('content.txt','r')
print(fopen.read())
fopen.close()
