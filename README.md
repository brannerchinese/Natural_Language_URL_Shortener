## URL Shortener

This project uses Chinese characters as the basis of shortened URLs. 

### To Install

 1. This is a Python3 project. The only dependency outside of the `requirements.txt` file is `sqlite3`.

 1. Enter the `url_shortener` directory and create database:

        sqlite3 shortener.db < create_shortener_database.sql

 1. Then run the web-application:

        python web_app.py

   and point a browser at `http://127.0.0.1:5000`. 

   Enter a URL in the text field and submit. The URL will be stored in a database and you will be given a new, short URL that will point to the original URL. The new URL will be of the form `http://127.0.0.1:5000/完`, where the "path" `完` stands for one or more Chinese characters.

### Ideas in Play

 1. There are roughly 2650 characters in the domain of the Hànyǔ Shuǐpíng Kǎoshì 漢語水平考試 (official "Chinese Proficiency Test" or HSK), up to level 6. These represent the characters appearing in the most common words of the Chinese language. The inventory of two-character strings that can be composed by combining any two of these indiscriminately is about seven million; three character strings number about 19 billion, and four character strings about 50 trillion. That means that strings or not more than four characters vastly outnumber the entire set of four-character strings that can be generated with the roughly 100 printable lower ASCII characters.

 1. We assume here that the purpose of shortened URLs is chiefly for human convenience, so it doesn't matter that each Chinese character is represented internally by a four-place hexadecimal sequence.

 1. Since this is a proof-of-concept, we are not concerned with scalability at this stage, so shortened paths are assigned randomly rather than by a reproducible hashing function. We are not concerned with duplicate URLs appearing in the database, either, since shortened strings are plentiful.

 1. Note that because these shortened strings are generated randomly, they are unlikely to be meaningful. However, since only very common characters are used, the strings should be readable by any literate person.

### To Do

 1. Handle paths when no corresponding URL found in the dictionary.

 1. Validate URLs, both as to form and as to accessibility, before storing.

 1. Can we keep statistics on usage?

 1. Add a table to the database to keep track of how many 1-char short forms there are, how many 2-char short forms, and so on. Eventually there will be no need to check for empty 1-char records.

 1. Add an `expiration_date` field to the `shortened_to_url` table, so that some shortened URLs can be deleted after a given date. There should be a way of keeping track of which shortned URLs have such dates, so that `shortened_to_url` can be pruned easily.
 1. Both traditional and simplified forms are available in `hsk.py`. Add the option to select one or the other set to the website. Better, select only those characters appearing in both lists — the intersection of the two contains 1692 characters.

[end]
