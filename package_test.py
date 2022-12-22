#create a folder: folder name (package name)
#create file named : __init__.py inside that folder and all subfolders
#dunder: __init__

#import numpy as np
#print(np.__file__)
  
import python_package as pp
# from python_package import test
# from python_package import test_again

import python_package.test as t
import python_package.test_again as ta
import python_package.package_python.test_test as tt #alias

'''
import python_package.test as t #broad concept - max
from python_package.test import hi #specific - memory low...
#from collections import Counter
'''
print("Dir: ",dir(tt))
#print("Doc: ",t.__doc__)
#print(help(t))
print("File: ",tt.__file__)
print("Name: ",tt.__name__)
#print("Path: ",tt.__path__)
print("Builtins: ",tt.__builtins__)

'''
#calling
#t.hello()
#t.hi()
#t.check()

ta.hello()
ta.check()
'''
#calling again
#hi()

#calling again
print("TestTest: ",tt.__file__)
tt.test_hello()
#quit()
