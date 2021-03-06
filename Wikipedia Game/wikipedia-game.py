from bs4 import BeautifulSoup
from random import randint
import urllib2
import urllib
import time
import re

wiki_url = "http://en.wikipedia.org"
wiki_param = "/wiki/"

def open_url(url):
        return BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")

def run_game(start_topic, key):
	page_url = wiki_url + wiki_param + urllib.quote(start_topic)
	
	checked_urls = []
	checked_urls.append(page_url)
	found = False
	while found == False:
		page = open_url(page_url)
		article_title = page.find_all('h1', id="firstHeading")[0].string
       	if article_title:
			print "Searching Article on: " + article_title
		else:
			print "Searching Article with url: " + urllib.unquote(page_url)

		wiki_links = []
		for a in page.find_all('a', href=True):
			if is_good_wiki_link(a['href'], checked_urls):
				wiki_links.append(a['href'])
		
		possible_finds = filter(lambda x: len(x) == len(key), page.body.find_all(text=re.compile(key, re.I)))
		if len(possible_finds) > 0:
			element = possible_finds[0].parent
	
			if article_title:
        		print "Success! Found word in article: " + article_title
			else:
				print "Success! Found word in article with url: " + urllib.unquote(page_url)
			
			print "HTML element: " 
			print element
			found = True		
		else:
			page_url = wiki_url + wiki_links[randint(0,len(wiki_links) - 1)]
			checked_urls.append(page_url)
			time.sleep(3)
			

def is_good_wiki_link(link, checked_urls):
	return ":" not in link and link.startswith("/wiki/") and (wiki_url + link) not in checked_urls

def start():
	topic_okay = False
	while topic_okay == False:
		try:
			topic = raw_input("Please enter a start page (topic): ")
		        page = urllib2.urlopen(wiki_url +  wiki_param + urllib.quote(topic.strip()))
		except urllib2.HTTPError, err:
			print "No page found for this topic, maybe you misspelled something?", err.code
		except urllib2.URLError, err:
			print "Some unknown error occurred...", err.reason
		else:
			topic_okay = True
	
	word_okay = False
	while word_okay == False:
       		word = raw_input("Please enter a word that you would like to search for: ")
		if len(word.strip()) > 0:
			word_okay = True

	run_game(topic.strip(), word.strip())

start()