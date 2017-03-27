import csv
import os

filename = 'content.json'
filenameTxt = 'content.txt'

#reading functions
#read()
#readlines()

#file modes : r, a , w, rb, r+, w+
#tell(): current position of file
#seek(): seek at given position of file

fp = open(os.path.dirname(os.path.abspath(__file__))+'/'+filenameTxt,'r+')

#reading
text = fp.read()
lines = fp.readlines()

print("Tell : ",fp.tell())
print("Seeking :", fp.seek(11)) 
print("Tell :", fp.tell())
print("Seeking :", fp.seek(16)) 
print("Tell :", fp.tell())

print(fp.read())

fp.close()

#Writing files
fw = open(os.path.dirname(os.path.abspath(__file__))+'/filetest.txt','w+')
fw.write("Testing Writing to Files")
fw.writelines("Testing Writing to Files again and \n using multiline \n this time")
fw.close()

#check file is empty then append
fo = open(os.path.dirname(os.path.abspath(__file__))+'/filetest.txt','a+')
fo.write("\n am appending to file now")
fo.close()