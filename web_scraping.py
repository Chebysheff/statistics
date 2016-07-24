# web_scraping.py
#
# Personal web scraping tools
#
# 
# To do:
# - parsing regex
# - internal and external url handling
# - error handling
# - crawl function


from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import datetime
import random
import re


def get_html(url): 
    try:
        page = urlopen(url)
        if page is None: 
            return url_list
    except (HTTPError, ValueError, URLError) as e:
        print("An error occured: {}. Unable to connect to {}".format(e, url))
        return url_list

    html = BeautifulSoup(page.read(), 'html.parser')
    return html


def get_urls(url, print_links=0, delimiter=0): # Fix features later
    url_list = []

    html = get_html(url) 
    anchors = html.findAll('a')
    
    for anchor in anchors:
        link = anchor.get('href')
        if link:
            url_list.append(link)

    return url_list


def get_internal_urls(url):
    url_list = []
     
    html = get_html(url)
    anchors = html.findAll('a', href=re.compile('^(\/|.*' + url + ')')) # Update regex for better parsing

    for anchor in anchors:
        link = anchor.get('href')
        if link and link not in url_list:
            url_list.append(link)

    return url_list


def get_external_urls(url):
    url_list = []
  
    html = get_html(url)
    anchors = html.findAll('a', href=re.compile("^(http|www)((?!" + url + ").)*$")) # Update regex for better parsing
    
    for anchor in anchors:
        link = anchor.get('href')
        if link and link not in url_list:
            url_list.append(link)

    return url_list

def split_url(url):
    address = url.replace('http://', '').strip('/')
    return address

def get_random_external_urls(url):
    pass

def crawl_external(url):
    pass

def crawl_internal(url):
    pass

def main():
    x = get_urls('http://google.com')
    print(x)


if __name__ == '__main__':
    main() 




