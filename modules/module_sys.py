"""
sys : system specific parameters and functions
Python Interpreter
"""
import sys #Python

#sys.argv: Command line argument  ex: python script.py argument argument

#Python: 3.7 add path!
print("sys.path :",sys.path) #PYTHONPATH

print("sys.version :",sys.version) #Python Version

print("sys.version_info :",sys.version_info) #Python Version_Info

print("sys.platform :",sys.platform)

#print("sys.modules_keys() :",sys.modules.keys())

print("sys.modules :",sys.modules) #Dictionary mapping modules etc

#print("sys.builtin_module_names :",sys.builtin_module_names) #Builtin Module Names

if sys.platform == "win32":
    import re
    print("Win32 platform Logic")
elif sys.platform == "mac":#darwin
    import os
    print("Mac Platform")
else:
    print("Platform Not Matched !!")

print("Exiting now!")
sys.exit(1) #old versions 
