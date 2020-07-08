from bs4 import BeautifulSoup
import requests

n = 10
base_url = "http://www.reddit.com"

text = requests.get(base_url).text
soup = BeautifulSoup(text)

# Print raw HTML (formatted for command line display compatibility) (Both below are valid ways)
# print(text.encode('ascii', 'ignore'))
# print(soup.prettify().encode('ascii', 'ignore')) # print in pretty format

# Print out full title HTML tag.
print(soup.title)

# Print type of HTML tag title is
print(soup.title.name)

# Print the content of the title HTML tag.
print(soup.title.string)

# Print first n links contained in document
for link in soup.find_all('a')[:n]:
	print(link.get('href'))
	print(link.get('class'))

# Filter out real links (user content) from all links and print these.	
real_links = filter(lambda x: 'may-blank' in x.get('class'), filter(lambda y: y.get('class') != None, soup.find_all('a')))
for link in real_links[:n]:
	print(link.get('href'))
	
# Suck out and print "real" text content from Reddit (no titles, html tags, etc.)
text_tags = soup.find_all('p') # 'p' is HTML paragraph tag
for tag in text_tags[:n]:
	print(tag.string)