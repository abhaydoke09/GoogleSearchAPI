from BeautifulSoup import BeautifulSoup
from twill import *
import re
import urllib
import requests

to_visit = []
blocked_urls=[
    'webcache.googleusercontent.com',
    '.pdf',
    '.doc',
    '.ppt',
    '.xml',
    '.ps',
    '.pps'
    ]


def check_link(web_link):
    for link in blocked_urls:
        if link in web_link:
            return False
    return True

def add_to_visit(links):
    pat = re.compile('"/url\?q=[^&]+&')
    for l in links:
        m = pat.search(str(l))
        if m is not None:
            web_link = m.group(0)[8:-1]
            web_link = urllib.unquote(web_link).decode('utf8')
            if web_link not in to_visit and check_link(web_link) :
                to_visit.append(web_link)

google_search_pages = []
search_query = 'india'

my_browser = get_browser()
my_browser.set_agent_string = 'Mozilla/5.0 (Windows NT 6.1; WOW64) Chrome/20.0.1092.0 Safari/536.6'
my_browser.go('http://www.google.co.in')

fv("2", "q", search_query)
my_browser.submit()
page = my_browser.get_html()
try:
    soup = BeautifulSoup(page, "html5lib")
    links = soup.find_all("h3", attrs={"class": "r"})
    add_to_visit(links)

    google_links = soup.findAll('a', class_='fl')
    for link in google_links:
        google_search_pages.append('http://www.google.co.in'+link.get("href"))
        if len(google_links) > 10:
            break

    for link in google_search_pages:
        my_browser.go(link)
        page = my_browser.get_html()

        soup = BeautifulSoup(page, "html5lib")
        links = soup.findAll('a')
        add_to_visit(links)

except Exception as ex:
    print "exception :" + str(ex)
    pass