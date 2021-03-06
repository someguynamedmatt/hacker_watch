import contextlib
import time
import sys
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup as bs
from urllib import request as req

@contextlib.contextmanager
def quitting(thing):
    """
    While 'thing' is present keep returning, quit when empty
    """
    yield thing
    thing.quit()

def initiate_webdriver(site, save_location):
    """
    Initialize webdriver (Firefox) and save page as screenshot
    """
    with quitting(webdriver.Firefox()) as driver:
        driver.implicitly_wait(10)
        driver.get(site)
        driver.get_screenshot_as_file(save_location)

def get_site_markup(site):
    """
    returns site markup via BeautifulSoup
    """
    markup = bs(req.urlopen(site), 'lxml')
    return markup

def is_username_found(markup, username):
    """
    Check all of the <a> tags for the passed-in username,
    returning True if found, False otherwise
    """
    for a_tag in markup.findAll('a'):
        if a_tag.text == username:
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('\n[ERROR]: Please supply username to search for and number of seconds to repeat. Exiting.\n')

    SITE = 'https://news.ycombinator.com/news'
    USERNAME = str(sys.argv[1])
    REPEAT_TIME = float(sys.argv[2])
    SAVE_LOCATION = './proof.png'

    def run():
        """
        main Run method
        """
        markup = get_site_markup(SITE)
        if is_username_found(markup, USERNAME):
            print('Username found!')
            initiate_webdriver(SITE, SAVE_LOCATION)
            sys.exit('Saved screenshot. My job here is done. Exiting\n')
        print('Hmmm. I didn\'t see it. Lemme try again in ' + str(REPEAT_TIME) + ' seconds.')

    STARTTIME = time.time()
    while True:
        print('Checking HackerNews for ' + USERNAME + '\'s post')
        run()
        time.sleep(REPEAT_TIME - ((time.time() - STARTTIME) % REPEAT_TIME))

