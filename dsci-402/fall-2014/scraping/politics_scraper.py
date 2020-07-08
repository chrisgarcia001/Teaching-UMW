from bs4 import BeautifulSoup
import requests

output_dir = 'data'

base_url = "http://www.nydailynews.com/blogs/dailypolitics"

n = 5

soup = BeautifulSoup(requests.get(base_url).text)
#print(soup.prettify().encode('ascii', 'ignore')) # print in pretty format

# Writes content 'text' to a file in specified directory with filename 'title'.txt
def write_page(dir, title, text):
	wfile = open(dir + "/" + title + '.txt', 'w')
	wfile.write(text)
	wfile.close()
	
#write_page("data", 'test', soup.prettify().encode('ascii', 'ignore'))

articles = soup.find_all('article')
#print(articles)

visited = 0
i = 0

while visited < min(n, len(articles)) and i < len(articles):
	try:
		link = articles[i].a.get('href')
		print('Scraping: ' + link)
		curr_soup = BeautifulSoup(requests.get(link).text)
		title = str(visited) + '.txt'
		#title = curr_soup.title.name.replace(" ", "_") + ".txt"
		text = ""
		for para in curr_soup.findAll('p'):
			try:
				text += "\n\n" + unicode(para.string or '').encode('ascii', 'ignore')
			except:
				text += ' '
		write_page(output_dir, title, text)
		print('Done!')
		visited += 1
	except:
		print("UNABLE TO SCRAPE!")
	i += 1
