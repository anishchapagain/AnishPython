"""
XPath: A syntax for identifying parts of an XML document
"""
from xml.etree import ElementTree
import xml.dom as dom
import xml.etree.ElementTree as ET
import os
import codecs


filename = os.path.dirname(os.path.abspath(__file__))+'/'+'nep_lang.xml'
file = codecs.open(filename,"r","utf-16-le")
xmlTree = ET.fromstring(file.encoding('utf-16-le'))

# xmlTree = ET.parse(fileTree)
# xmlTree = ET.parse(filename)

#Root Element
root = xmlTree.getroot()
rootTag = root.tag
rootAttrib = root.attrib
print(rootTag)
print(rootAttrib)

#Nodes
for node in root.findall('.//cesHeader/fileDesc/titleStmt'): #XPath
    title = node.tag
    print(title)
    childTags = [child.tag for child in node.iter()]
    print("Child Tags : ",childTags)

    for tags in node.findall('respStmt'):
        print(tags.find('respName').text ," >> ",tags.find('respType').text)
    