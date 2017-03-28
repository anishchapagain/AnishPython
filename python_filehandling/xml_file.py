"""
http://www.diveintopython3.net/xml.html
"""
from xml.dom import minidom
import os

xmlfile=os.path.dirname(os.path.abspath(__file__))+'/staff.xml'
doc = minidom.parse(xmlfile)

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")[0]
print("Node Name : %s" % name.nodeName)
print("Name Data :",name.firstChild.data)
print("Name FirstChild :",name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))