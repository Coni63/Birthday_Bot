###Happy Birthday Bot

Based on [this website](https://anniversaire-celebrite.com/), I want to extract data and store them in a SQLite database. This database is after used to wish a Happy birthday on twitter if they have a certified account. 

In Extraction.ipynb, they is all phase of scrapping (initial scrap / update / corrections).
In Exploration.ipynb, there is a simple exploration of the current database

The bot is now active at [this link](https://twitter.com/HBirthday_Bot "this link").

A small Flask Website have been created also at [this link](http://nicolasmine.pythonanywhere.com/ "this link") to propose new celebrities. For now, based on the exploration, I'll only consider French propositions.

The website is also avaialble in folder website.

The only missing file is key.txt to place in site/ folder and the structure should be the following one:

```python
CONSUMER_KEY:ABCDE
CONSUMER_SECRET:ABC123456
ACCESS_KEY:ZYXWVU
ACCESS_SECRET:ZYX987654
```

All keys should be requested on twitter API so are not publicly available.