import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

times = int(input('Enter times'))
position = int(input('Enter position'))

cur = 0

while cur < times:
	tag = tags[position - 1]
	ans = tag.contents[0]
	url = tag.get('href', None)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	cur = cur + 1

print(ans)