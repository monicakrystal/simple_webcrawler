import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


def start_webcrawl():
    url = ''
    html = urllib.request.urlopen(url).read()
    soups = BeautifulSoup(html, 'html.parser')
    for soup in soups:
        print(soup)



if __name__ == '__main__':
    start_webcrawl()

