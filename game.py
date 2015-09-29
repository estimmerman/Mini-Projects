from bs4 import BeautifulSoup
from random import randint
import urllib2
import urllib
import time
import re

def open_url(url):
        return BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")

def run_game(start_topic, key):
	wiki_url = "http://en.wikipedia.org"
	wiki_param = "/wiki/"
	
	page_url = wiki_url + wiki_param + urllib.quote(start_topic)
	
	found = False
	while found == False:
		page = open_url(page_url)
		article_title = page.find_all('h1', id="firstHeading")[0].string
                print "Searching Article on: " + article_title

		wiki_links = []
		for a in page.find_all('a', href=True):
			if is_good_wiki_link(a['href']):
				wiki_links.append(a['href'])
	
		print page.body.find_all(text="the")
		if len(page.body.find_all(text=re.compile(key))) > 0:
			print "Success! Found word in article: " + article_title
			found = True		
		else:
			page_url = wiki_url + wiki_links[randint(0,len(wiki_links) - 1)]
			time.sleep(3)

def is_good_wiki_link(link):
	return ":" not in link and link.startswith("/wiki/")


run_game("World War II", "global")

