import xml.etree.ElementTree as ET
import urllib
import urllib.request
from urllib.request import urlopen
x = input("Enter location:")
print("Retrieving",x)

xml = urllib.request.urlopen(x).read()
stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment/count')

sum = 0

for item in lst:
    sum = sum + int(item.text)

print("Count :",len(lst))
print("Sum :", sum)
