from bs4 import BeautifulSoup
import requests

output_dir = 'data'

base_url = "http://www.reddit.com"

n = 10

soup = BeautifulSoup(requests.get(base_url).text)

def write_page(dir, title, text):
	wfile = open(dir + '/' + title + '.txt', 'w')
	wfile.write(text)
	wfile.close()

real_links = filter(lambda x: 'may-blank' in x.get('class'), filter(lambda y: y.get('class') != None, soup.findAll("a")))

visited = 0
i = 0

while visited < min(n, len(real_links)):
	link = real_links[i]
	url = link.get('href')
	try:
		curr_soup = BeautifulSoup(requests.get(url).text)
		title_tag = curr_soup.title
		title = str(visited + 1)
		text = ''
		print title
		for para in curr_soup.findAll('p'):
			text += "\n\n" +  (para.string or '')
		visited += 1
		write_page(output_dir, title, text)
	except:
		print('Unable to read page: ' + url)
	i += 1
	