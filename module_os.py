import os
import sys
import time
import stat

def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print("- size:", size, "bytes")
    #print("- owner:", uid, gid)
    print("- created:", time.ctime(ctime))
    print("- last accessed:", time.ctime(atime))
    print("- last modified:", time.ctime(mtime))
    #print("- mode:", oct(mode))
    #print("- inode/dev:", ino, dev)


print(os.sep)

print('__file__ : ',__file__)

print('os.getcwd() : ',os.getcwd())

print(os.path.join(os.sep,'home','dir','test'))

print('os.path.curdir :', os.path.curdir)
print('os.path.isdir :', os.path.isdir(os.path.realpath(__file__)))
print('os.path.isfile :', os.path.isfile(os.path.realpath(__file__)))
print('os.path.exists :', os.path.exists(os.path.curdir))
print('os.path.splittext :', os.path.splitext(os.path.realpath(__file__)))
print('os.path.dirname(__file__) : ',os.path.dirname(__file__))
print('os.path.realpath(__file__) : ',os.path.realpath(__file__))
print('os.path.abspath(__file__) : ',os.path.abspath(__file__))  
print('os.path.basename(__file__) : ',os.path.basename(__file__))
print('os.path.getmtime : ',time.ctime(os.path.getmtime(__file__)))

dump(os.stat(__file__))