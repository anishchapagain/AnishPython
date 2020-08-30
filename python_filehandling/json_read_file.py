import json
import os
import shutil

#http://jsonlines.org/ #new
#https://json.org

#https://jsonformatter.org/
#https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson

#xml: ML (Tag), data- container, tag: attribute, XPath


data ={'a':'20.54','c':19.999,'b':[1,2,3,4]}
print(data)
print(type(data))

'''
[
{"elongitude":86.28,"elatitude":27.74,"epicentre":"Dolakha","etime":"18:02","emagnitude":4.2,"edate":"2015/06/26"},
{"elongitude":86.28,"elatitude":27.74,"epicentre":"Dolakha","etime":"18:02","emagnitude":4.2,"edate":"2015/06/26"}
]
'''
'''
{"addresses": [{"address_string": "1501 West Eleventh Place, Big Spring, TX 79720", "city": "Big Spring",
                "languages": [{"name": "English", "type": "primary"}], "office_name": "", "phones": [],
                "state": "TX", "street_line_1": "1501 West Eleventh Place", "street_line_2": "",
                "zip": "79720"}],
 "group_affiliations": [],
 "hospital_affiliations": [{"name": "Smmc Medical Group"}],
 "networks": [{"name": "TX Medicare Advantage", "tier": null}],
 "provider": {"accepting_new_patients": true, "facility_name": null, "first_name": "Ashutosh",
              "gender": "M", "last_name": "Rastogi", "license_number": "", "middle_name": "",
              "npi": "", "pcp": null, "pcp_id": null, "provider_type": "individual",
              "rating": {"scale": null, "score": null},
              "site_uid": "{D331FCEF-F618-446A-8217-74E4EE0C17C2}", "suffix": "DMD",
              "title": null, "unparsed_name": "Ashutosh Rastogi"},
 "specialties": [{"name": "Hematology"}]}

 TASK: Full Name, Phone Number!
'''


writefile = 'writeto.json'

#read from Json File
print("Read from JSON file-----------------\n")
with open(os.path.dirname(os.path.abspath(__file__))+'/'+'contentnew.json') as jsonFile: #r, r+  #raw:
    jf = json.load(jsonFile)
    print(jf['provider'])
    #print(jf)
    #print(jf['menu'])
    '''print(jf['menu']['header'])
    print(jf['menu']['items'][0]['id'])
    print(jf['menu']['items'][5])
    print(jf['menu']['itemsMenu']['OpenMenu']['id'])
    print(jf['menu']['items'][6])#None'''
    
quit()


#write a Dict to json file
print("\nWrite to New Json File---------------")
with open(os.path.dirname(os.path.abspath(__file__))+'/'+writefile, 'w') as fw:
    json.dump(data,fw)

quit()


#read from written file
print("\nReading Created JSON with Attributes--------------\n")
with open(os.path.dirname(os.path.abspath(__file__))+'/'+writefile, 'r') as fr:
    jr = json.load(fr)
    print(jr)
    #print(jr['c'])
    print(json.dumps(jr, indent=2)) #json beautify , indent=space
    print(json.dumps(jr, indent=4,sort_keys=True))


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

