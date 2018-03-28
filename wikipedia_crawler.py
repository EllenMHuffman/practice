from time import sleep
import urllib

import requests
from bs4 import BeautifulSoup


def continue_crawl(search_history, target_url, max_steps=25):
    '''
    Deterimine if the crawler should continue moving through pages.

    search_history = list of the pages already visited
    target_url = the goal url the crawler is trying to reach
    max_steps = optional, crawler will abort if max steps is reached
    '''

    if search_history[-1] == target_url:
        print("Target acquired!")
        return False
    elif len(search_history) > max_steps:
        print("Too many steps!")
        return False
    elif len(set(search_history)) != len(search_history):
        print("Stuck in a loop!")
        return False
    else:
        print("Continuing search...")
        return True


def find_first_link(url):
    '''
    Download html of last article in article_chain
    Find the first link in that html
    Use external packages requests and BeautifulSoup
    '''

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # This nested div contains the article's body
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link, or will remain as none
    article_link = None

    # find all direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # find first anchor tag in direct child of a paragraph
        # other types of links may be in other children that we don't want
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

################################################################################

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_url]


def web_crawl(start_url, target_url):
    while continue_crawl(article_chain, target_url):
        print(article_chain[-1])

        first_link = find_first_link(article_chain[-1])
        if not first_link:
            print("We've arrived at an article with no links, aborting search!")
            break

        article_chain.append(first_link)
        # delay for about two seconds
        sleep(2)


web_crawl(start_url, target_url)
