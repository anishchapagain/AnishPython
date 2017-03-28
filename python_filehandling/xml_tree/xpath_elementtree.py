"""
XPath: A syntax for identifying parts of an XML document
"""
from xml.etree import ElementTree
import os

with open(os.path.dirname(os.path.abspath(__file__))+'/'+'xml_elementtree.xml', 'r+') as f:
    xmlTree = ElementTree.parse(f)

for node in xmlTree.findall('.//outline/outline'): #XPath
    url = node.attrib.get('xmlUrl')
    print(url)