import json
import os

data = [{'a':'20.54','c':19.999,'b':[1,2,3,4]}]
print("Data :",data)
print("Str Data :", str(data))

jsonDump = json.dumps(data)
print("jsonDump Dump - Encode : ",jsonDump)

jsonLoad = json.loads(jsonDump)
print("jsonLoad Load - Decode : ",jsonLoad)

print("jsonDump Sort : ",json.dumps(data,sort_keys=True)) #sort. Sort two Json and Compare
print("jsonDump Sort : ",json.dumps(data,sort_keys=True,indent=3)) #indent no of spaces

print('repr(data) : ', len(repr(data)))
print('dumps(data) : ', len(json.dumps(data)))
print('dumps(data, indent=2)  :', len(json.dumps(data, indent=2)))
print('dumps(data, separators):', len(json.dumps(data, separators=(',',':'))))

print(jsonDump[2])
quit()
encoder = json.JSONEncoder()
for element in encoder.iterencode(data):
    print("Element : ",element)