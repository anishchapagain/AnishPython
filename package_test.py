import python_package as pp
# from python_package import test
# from python_package import test_again
import python_package.test as t
import python_package.test_again as ta
import python_package.package_python.test_test as tt
from python_package.test import hi

print("Dir: ",dir(pp))
print("Doc: ",pp.__doc__)
print("File: ",pp.__file__)
print("Name: ",pp.__name__)
print("Path: ",pp.__path__)
#print("Builtins: ",pp.__builtins__)

#calling
t.hello()
ta.hello()

#calling again
hi()

#calling again
print("TestTest: ",tt.__file__)
tt.test_hello()
quit()