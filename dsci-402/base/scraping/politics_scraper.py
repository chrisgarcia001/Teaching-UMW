from bs4 import BeautifulSoup
import requests

output_dir = 'data'

base_url = "http://www.nydailynews.com/blogs/dailypolitics"

n = 5

soup = BeautifulSoup(requests.get(base_url).text)

def write_page(dir, title, text):
	wfile = open(dir + '/' + title + '.txt', 'w')
	wfile.write(text)
	wfile.close()


# Note all "real" links are embedded inside an "article" element which contains one link.
# Select just these for exploration:
articles = soup.findAll("article")
#print(articles)

visited = 1
i = 1

while visited <= min(n, len(articles)) and i <= len(articles):
	try:
		link = articles[i].a.get('href')
		print('Scraping: ' + link + '...')
		curr_soup = BeautifulSoup(requests.get(link).text)
		#print(curr_soup)
		title = str(visited)
		text = ''
		for para in curr_soup.findAll('p'):
			#print(unicode(para).encode('ascii', 'ignore'))
			try:
				text += "\n\n" +  unicode((para.string or '')).encode('ascii', 'ignore')
			except:
				text += ' '
		#print(text)
		write_page(output_dir, title, text)
		print('Done!')
		visited += 1
	except:
		print('UNABLE TO SCRAPE!')
	i += 1

