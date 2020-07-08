from bs4 import BeautifulSoup
import requests

base_url = "http://www.reddit.com"
n = 10

soup = BeautifulSoup(requests.get(base_url).text)

# Print the full HTML title tag
print(soup.title)

# Print the tag name
print(soup.title.name)

# Print the actual text of the tag
print(soup.title.string)

# Print first n links contained in document
for link in soup.find_all('a')[:n]:
    print(link.get('href'))
	
# Note menu items have class='choice' and "real" articles have class='title may-blank '
# Filter just the "real" articles trending
real_links = filter(lambda x: 'may-blank' in x.get('class'), filter(lambda y: y.get('class') != None, soup.findAll("a")))
for link in real_links[:n]:
    print(link.get('href'))
	
# Suck out and print "real" text from Reddit (no titles, html, etc. - just real text content)
text_tags = soup.find_all('p') # 'p' is an HTML paragraph tag
for tag in text_tags[:n]:
	print(tag.string)