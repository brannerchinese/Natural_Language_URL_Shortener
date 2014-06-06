## Natural Language URL Shortener

URL shorteners usually assign you a "path" (the final segment of a URL other than any parameters) that is either a hash or a string of your own choosing. Hashes are hard to remember and strings aren't usually very short.

Instead, I found a way to produce paths that are always short but still easy to remember because they draw on natural language. Can you guess how?

### Background

I built this as part of the [Iron Forger exercise](https://hackpad.com/Iron-Forger-kEmauANGcV5) that a few [Hacker School](http://hackerschool.com) alums did to keep our teeth sharp during the summer of 2014 — the goal being to complete one project a week for eight weeks. The original project assignment was on [this Hackpad](https://hackpad.com/Build-a-url-shortener-JbagqacCoon) (accessed 20140526) and the initial working prototype was constructed in a few hours one late afternoon and early evening.

### Spoiler (decode as ROT13)

Guvf cebwrpg hfrf Puvarfr punenpgref nf gur onfvf bs fubegrarq HEYf. 

### To Install

 1. This is a Python3 project and you are assumed to be using a `virtualenv` virtual environment. The only dependency outside of the `requirements.txt` file is `sqlite3`.

 1. Enter the `url_shortener` directory and create the database:

        sqlite3 url.db < create_url_database.sql

 1. Then run the web-application:

        python web_app.py

   the response should be

         * Running on http://127.0.0.1:5000/
         * Restarting with reloader
   
 1. Point a browser at `http://127.0.0.1:5000`. 

 1. Enter a URL in the text field and submit. The URL will be validated and stored in a database and you will be given a new, short URL that will point to the original URL. The new URL will be of the form `http://127.0.0.1:5000/完`, where the "path" `完` stands for one or more Chinese characters.

### Ideas in Play

 1. There are roughly 2650 characters in the domain of the Hànyǔ Shuǐpíng Kǎoshì 漢語水平考試 (official "Chinese Proficiency Test" or HSK), up to level 6. These represent the characters appearing in the most common words of the Chinese language. The inventory of two-character strings that can be composed by combining any two of these indiscriminately is about seven million; three character strings number about 19 billion, and four character strings about 50 trillion. That means that strings of not more than four characters vastly outnumber the entire set of four-character strings that can be generated with the roughly 100 printable lower ASCII characters.

 1. We assume here that the purpose of shortened URLs is chiefly for human convenience, so it doesn't matter that each Chinese character is represented internally by a four-place hexadecimal sequence.

 1. Since this is a proof-of-concept, we are not concerned with scalability at this stage, so shortened paths are assigned randomly rather than by a reproducible hashing function. We are not concerned with duplicate URLs appearing in the database, either, since shortened strings are plentiful.

 1. Note that because these shortened strings are generated randomly, they are unlikely to be meaningful. However, since only very common characters are used, the strings should be readable by anyone literate in Chinese.

### Small features

 1. URL-validation is done empirically by trying to load the proposed URL, rather than by analyzing its form.
 1. Paths that do not exist in the database return an error message at the top of the `index.html` page.


### To Do

 1. Add an `expiration_date` field to the `shortened_to_url` table, so that some shortened URLs can be deleted after a given date. There should be a way of keeping track of which shortened URLs have such dates, so that the table can be pruned easily.

 1. Both traditional and simplified forms are available in `hsk.py`. There are 2671 of the former and 2635 of the latter, though the same morphemes are being represnted with both sets. Add the option to select one or the other set to the website. 

 1. Better, select only those characters appearing in both Chinese character-lists — the intersection of the two contains 1692 characters. Those characters are neutral with respect to the traditional-simplified divide.

 1. Use `urllib.request.urlopen(url).geturl()` to find actual URL received back from the request. Use that for another table in database: true URL to short path, in order to avoid redundant entries.

 1. Add a table to the database to keep track of how many 1-char short forms there are, how many 2-char short forms, and so on. Once the database begins to fill there will be no need to check for empty 1-char records.

 1. Keep statistics on when short URLs are used.

[end]
