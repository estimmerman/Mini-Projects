from bs4 import BeautifulSoup
from random import randint
import urllib2
import urllib

def open_url(url):
        return BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")

def run_game(start_topic, key):
	wiki_url = "http://en.wikipedia.org"
	wiki_param = "/wiki/"
	
	page_url = wiki_url + wiki_param + urllib.quote(start_topic)
	print "Searching Article on: " + urllib.unquote(page_url)
	
	notFound = True
	while notFound:
		page = open_url(page_url)
		article_title = page.find_all('h1', id="firstHeading")[0].string
                print "Searching Article on: " + article_title

		wiki_links = []
		for a in page.find_all('a', href=True):
			if is_good_wiki_link(a['href']):
				wiki_links.append(a['href'])
	
		if len(page.body.find_all(text=key)) > 0:
			print "Success! Found word in article: " + urllib.unquote(page_url)
			notFound = False		
		else
			page_url = wiki_url + wiki_links[randint(0,len(wiki_links) - 1)]


def is_good_wiki_link(link):
	return ":" not in link and link.startswith("/wiki/")


run_game("World War II", "bee")

