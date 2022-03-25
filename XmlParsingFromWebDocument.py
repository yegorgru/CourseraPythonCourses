import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Enter url')

fhand = urllib.request.urlopen(url)

input = fhand.read()

stuff = ET.fromstring(input)
lst = stuff.findall("comments/comment")
print('Comment count', len(lst))
s = 0
for item in lst:
	s = s + int(item.find('count').text)

print(s)