import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


def start_webcrawl(link):
    string_soup = ""
    with open(link) as file_of_websites:
        for website in file_of_websites:
            url = website.strip()
            html = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(html, 'html.parser')
            string_soup += str(soup)
    return string_soup

def write_names(lines, file_name_to_write_to):
    with open(file_name_to_write_to, "w") as f:
        f.write(lines)

if __name__ == '__main__':
    crawl_results = start_webcrawl('five_urls.txt')
    write_names(crawl_results, 'copied_html.txt')

