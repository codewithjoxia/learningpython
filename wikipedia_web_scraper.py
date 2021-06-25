## Wikipedia Web Scraper

# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import random

def scrapewikiarticle(url):
    response = requests.get(
        url=url,
    )
    # print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id='firstHeading')
    print (title.text)

    # Get all the links
    all_links = soup.find(id="bodyContent").find_all("a")
    random.shuffle(all_links)
    link_to_scrape = 0

    for link in all_links:

        print (link)
        # Get only links to other Wiki articles
        if link['href'].find("/wiki") == -1:
            continue

        # Use this link to scrape
        link_to_scrape = link
        break
    
    
    scrapewikiarticle("https://en.wikipedia.org" + link_to_scrape["href"])

scrapewikiarticle('https://en.wikipedia.org/wiki/Web_scraping')