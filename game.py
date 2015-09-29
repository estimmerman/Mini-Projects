from bs4 import BeautifulSoup
from random import randint
import urllib2
import urllib

def open_url(url):
        return BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")

def run_game(start_topic, key):
	wiki_url = "http://en.wikipedia.org/wiki/"
	page_url = wiki_url + urllib.quote(start_topic)
	found = False
	while(found == False):
		page = open_url(page_url)
		wiki_links = []
		for a in page.find_all('a', href=True):
			if "/wiki/" in a['href']:
				wiki_links.append(a['href'])
		page_url = wiki_url + wiki_links[randint(0,len(wiki_links) - 1)]
		print page_url
		found == True


run_game("World War II", "bee")

