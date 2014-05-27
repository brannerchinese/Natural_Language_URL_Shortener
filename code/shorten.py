#! /usr/bin/env python
# shorten.py
# David Prager Branner
# 20140527, works.

import sqlite3
import random

"""Using kanji, generate a string for use as the path in a shortened URL."""

# Generate a randomly shuffled list of all kanji in Unicode Plane 0.
# Valid codepoints range from hex 3400:9FFF i.e. decimal 13312:40959, inclusive.
codepoints = list(range(13312, 40960))


def shorten(url, db='shortener.db'):
    """Return a unique string to represent input string url."""
    connection = sqlite3.connect('../' + db)
    with connection:
        cursor = connection.cursor()
        path = get_path(cursor, url)
    return path

def get_path(cursor, url):
    """Try 20 times to get, at random, an empty slot for a one-digit path.

    If that fails, try two digits, etc."""
    prospective_shortened = None
    n = 1
    while prospective_shortened == None:
        for i in range(20):
            prospective_shortened = ''.join(
                    [chr(random.choice(codepoints)) for i in range(n)])
            # Try to insert; IntegrityError means already exists.
            try:
                cursor.execute(
                        '''INSERT INTO shortened_to_url (shortened, url)'''
                        '''VALUES (?,?)''', (prospective_shortened, url)
                        )
                break
            except sqlite3.IntegrityError:
                prospective_shortened = None
                continue
        n += 1
    return prospective_shortened
