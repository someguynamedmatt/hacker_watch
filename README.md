# Obsessively monitor HackerNews!
> Please set the retry time responsibly. Don't spam the site.
---

`python hacker_watch.py "myusername" 1200` // This example will search for `myusername` every 30 mins

This will watch `news.ycombinator.com/news` (first page only), and save a screenshot of the page if it finds a username that it's passed.
> Will default save `proof.png` to whichever directory it's initialized from

Required args:

- username (`str`)
- time to retry in seconds (`float`)



