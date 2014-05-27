## URL Shortener

This project uses Chinese characters ("kanji", as a shorthand name) as the basis of shortened URLs. 

### To Install

 1. This is a Python3 project. The only dependency outside of the `requirements.txt` file is `sqlite3`.

 1. Create database:

        sqlite3 shortener.db < code/create_shortener_database.sql

 1. Run web-application:

        python code/web_app.py

### Ideas

 1. There are some 27K kanji in Unicode Plane 0, so far fewer of them are needed than ASCII to generate the same number of strings of a given length: two-kanji strings number over 76M and three-kanji strings over 21T. We assume here that the purpose of shortened URLs is chiefly for human convenience, so it doesn't matter that each kanji is represented internally by a four-place hexadecimal sequence.

 1. Since this is a proof-of-concept, we are not concerned with scalability at this stage, so shortened paths are assigned randomly rather than by a recoverable hashing function. We are not concerned with duplicate URLs in the database, either, since shortened strings are plentiful.

 1. Note that because the shortened strings are generated randomly, they are unlikely to be meaningful.

### To Do

 1. Add a table to the database to keep track of how many 1-char short forms there are, how many 2-char short forms, and so on. Eventually there will be no need to check for empty 1-char records.

 1. Add an `expiration_date` field to the `shortened_to_url` table, so that some shortened URLs can be deleted after a given date. There should be a way of keeping track of which shortned URLs have such dates, so that `shortened_to_url` can be pruned easily.

[end]
