#! /usr/bin/env python
# shorten.py
# David Prager Branner
# 20140527

import sqlite3
import random

"""Use kanji as basis of shortened URLs."""

# Generate a randomly shuffled list of all kanji in Unicode Plane 0.
# Valid codepoints range from hex 3400:9FFF i.e. decimal 13312:40959, inclusive.
codepoints = list(range(13312, 40960))


def shorten(url, db='shortener.db'):
    """Return a unique string to represent input string s."""
    # Idea: since the purpose of shortening is for human convenience, use
    # random strings of Chinese characters rather than ASCII.
    connection = sqlite3.connect('../' + db)
    with connection:
        cursor = connection.cursor()
        path = get_path(cursor, url)
        # If kanji already in use, must generate new string of >1 kanji.
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
            print('{}: {}'.format(n, prospective_shortened), end=' ')
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
    print('successful')
    return prospective_shortened

# To do: add a table to keep track of how many 1-char short forms there are ,
# how many 2-char short forms, and so on. Eventually there will be no need to
# check for empty 1-char records.
