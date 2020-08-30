"""
Retrieve all of the metadata for one member of an archive.
"""
#end_pymotw_header

import zipfile
import os

print('__file__ : ',__file__)
print('os.getcwd() : ',os.getcwd())
print('os.path.dirname(__file__) : ',os.path.dirname(__file__))
print('os.path.realpath(__file__) : ',os.path.realpath(__file__))
print('os.path.abspath(__file__) : ',os.path.abspath(__file__))  
print('os.path.basename(__file__) : ',os.path.basename(__file__))
print("\n")

with zipfile.ZipFile(os.path.dirname(__file__)+'/example.zip') as zf:
    for filename in [ 'README.txt', 'notthere.txt' ]:
        try:
            info = zf.getinfo(filename)
        except KeyError:
            print('ERROR: Did not find %s in zip file' % filename)
        else:
            print('%s is %d bytes' % (info.filename, info.file_size))
