"""
Parsed XML documents are represented in memory by ElementTree and Element objects connected into a tree
structure based on the way the nodes in the XML document are nested
"""
from xml.etree import ElementTree
import os

with open(os.path.dirname(os.path.abspath(__file__))+'/'+'xml_elementtree.xml', 'r+') as f:
    xmlTree = ElementTree.parse(f)

for node in xmlTree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    if name and url:
        print('  %s :: %s' % (name, url))
    else:
        print(name)
