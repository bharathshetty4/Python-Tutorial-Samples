from xml.dom import minidom

f = open('pets.txt', 'r')
pets = minidom.parseString(f.read())
f.close()

names = pets.getElementsByTagName('name')
for name in names:
	print (name.firstChild.nodeValue)

#json format read


import json
from pprint import pprint

f = open('pets_json.txt', 'r')
pets = json.loads(f.read())
f.close()

print(pets)
