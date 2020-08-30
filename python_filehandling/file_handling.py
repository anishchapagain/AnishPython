#RAW:Read Append Write (modes)
#Create: Write->Append
#modes (+) : extra task
import os

filename = 'content.json'
filenameTxt = 'content.txt'

#open(filepath,mode): main function
#reading functions
#read()
#readlines()
#close()

#file modes : r, a , w, rb, r+, w+
#tell(): current position of file
#seek(): seek at given position of file

fp = open(os.path.dirname(os.path.abspath(__file__))+'/'+filenameTxt,'r+')#recc
#fp = open('e:\AnacondaPythonScripts\Python_Tutorial\PythonNotes\modules\content1.txt','r')#not recc

#reading line by line
for lineno,text in enumerate(fp.readlines()):
    print("{} -- {}\n".format((lineno+1),text))


#reading: read(), readline(), readlines(), read(50): num of char
#text = fp.read()
lines = fp.readlines() #TASK1: File was already read
#line1 = fp.readline() 
#print(text)
print(lines)
#print(line1)
#line2 = fp.readline()
#print(line2)
#print("Length: ",len(lines))

print("Tell : ",fp.tell()) #position show
print("Seeking :", fp.seek(11)) #cursor..position ..placing
print("Tell :", fp.tell())
print("Seeking :", fp.seek(16)) 
print("Tell :", fp.tell())

#print(fp.read())
#print(fp.readlines())

fp.close()


#Writing files: create and write
fw = open(os.path.dirname(os.path.abspath(__file__))+'/filetest.txt','w+')
fw.write("Testing Writing to Files")
fw.writelines("\nTesting Writing to Files again and \n using multiline \n this time")
fw.close()


#check file is empty then append
fo = open(os.path.dirname(os.path.abspath(__file__))+'/filetest.txt','a+')
fo.write("\n ##am appending to file now")
fo.write("\n ##APPENDED Content!") #position 61 insert? TASK2#
fo.close()


#inserting content in between!
fo = open(os.path.dirname(os.path.abspath(__file__))+'/filetest.txt','r+')
fo.seek(200)
fo.write("\n ##Inserting using read+ mode## -- ") #position 61 insert? TASK2#
fo.seek(0)
print(fo.read())
fo.close()
