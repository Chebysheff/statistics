# web_scraping.py
#
# Personal web scraping tools

import bs4, requests

def get_urls(urls, print_links=0):
    url_list = []

    for url in urls:
        try:
            page = requests.get(url)
            page.raise_for_status()
        except Exception as exc:
            print("An error occured: {}".format(exc))
            continue

        content = bs4.BeautifulSoup(page.text, 'html.parser') # Parse content

        for link in content.find_all('a'):
            found = link.get('href')
            url_list.append(found)

            if print_links:
                print(found)
    
    return url_list


def main():
    urls = ['http://www.google.com']
    links = get_urls(urls)

if __name__ == '__main__':
    main() 
          

       

       
