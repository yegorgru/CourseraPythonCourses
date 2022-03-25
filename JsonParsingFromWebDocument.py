import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter url')

fhand = urllib.request.urlopen(url)

input = fhand.read()

info = json.loads(input)
lst = info["comments"]
print('Comment count', len(lst))
s = 0
for item in lst:
	s = s + int(item["count"])

print(s)