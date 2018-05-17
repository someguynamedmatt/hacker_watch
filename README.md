# Obsessively monitor HackerNews!
---

`python hacker_watch.py "myusername" 1200` // This example will search for `myusername` every 30 mins

This will watch `news.ycombinator.com/news` (first page only), and save a screenshot of the page if it finds a username that it's passed.

> Will default save to whichever directory it's run from

Required args:

- username (`str`)
- time to retry in seconds (`float`)



