import contextlib
import sys
import selenium.webdriver as webdriver
from urllib import request as req
from bs4 import BeautifulSoup as bs


@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()

def initiate_webdriver(site, save_location):
    with quitting(webdriver.Firefox()) as driver:
        driver.implicitly_wait(10)
        driver.get(site)
        driver.get_screenshot_as_file(save_location)

def get_site_markup(site):
    markup = bs(req.urlopen(site), 'lxml')
    return markup

def is_username_found(markup, username):
    for a in markup.findAll('a'):
        if a.text == username:
            return True
    return False

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 2:
        sys.exit('\n[ERROR]: Please supply username to search for. Exiting.\n')

    SITE = 'https://news.ycombinator.com/news'
    USERNAME = sys.argv[1]
    SAVE_LOCATION = "./proof.png"

    markup = get_site_markup(SITE)
    if is_username_found(markup, USERNAME) is True:
        print('Username found!')
        initiate_webdriver(SITE, SAVE_LOCATION)







