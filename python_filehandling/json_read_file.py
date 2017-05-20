import json
import os
import shutil

data = {'a':'20.54','c':19.999,'b':[1,2,3,4]}
print(data)
print(type(data))

writefile = 'writeto.json'

#read from Json File
print("Read from JSON file-----------------\n")
with open(os.path.dirname(os.path.abspath(__file__))+'/'+'content.json', 'r+') as ff:
    jf = json.load(ff)
    print(jf)
    print(jf['menu']['header'])
    print(jf['menu']['items'][0]['id'])
    print(jf['menu']['items'][5])
    print(jf['menu']['items'][6])#None

#write a Dict to json file
print("\nWrite to New Json File---------------")
with open(os.path.dirname(os.path.abspath(__file__))+'/'+writefile, 'w+') as fw:
    json.dump(data,fw)

#read from written file
print("\nReading Created JSON with Attributes--------------\n")
with open(os.path.dirname(os.path.abspath(__file__))+'/'+writefile, 'r+') as fr:
    jr = json.load(fr)
    print(jr)
    print(json.dumps(jr, indent=2))
    print(json.dumps(jr, indent=2,sort_keys=True))

#copy original first: .bak
print("Taking Backup before Updating")
shutil.copyfile(os.path.dirname(os.path.abspath(__file__))+'/'+'content.json',os.path.dirname(os.path.abspath(__file__))+'/'+'content.json_bak')

#Task: try to update the value items[0]['label']
print("\nUpdating JSON------------------\n")
#read from Json File
with open(os.path.dirname(os.path.abspath(__file__))+'/'+'content.json', 'r+') as f:
    j = json.load(f)
    a = j['menu']['items'][0]['id']
    print("j['menu']['items'][0] : " , j['menu']['items'][0])
    print("j['menu']['items'][1] : " , j['menu']['items'][1])
    print("j['menu']['items'][0]['id'] : " , a)
    j['menu']['items'][0]['label']=''
    print("j['menu']['items'][0] : " , j['menu']['items'][0])

    #Updating: Try with Index [2] , re-write any node with {'id':'','value':''}
    j['menu']['items'][2]['id']='No2' #then assign the Value as required
    j['menu']['items'][2]['label']='No2 Label' #then assign the value as required

    f.seek(0)
    json.dump(j,f,indent=2)

    # del(j['menu']['items'][2]) #delete any index first