"""
http://www.diveintopython3.net/xml.html
"""
from xml.dom import minidom
import os

xmlfile=os.path.dirname(os.path.abspath(__file__))+'/staff.xml'
doc = minidom.parse(xmlfile) #~ json.dumps(file,indent=)

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")[0]

#print("Node Name : %s" % name.nodeName) #1print...format
print("Node Name : ",name.nodeName)#2
print("Node Name : {}".format(name.nodeName))#3
print(f"Node Name : {name.nodeName}")#4

print("Name Data :",name.firstChild.data)
print("Name FirstChild :",name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))
