#! /usr/bin/env python
# shorten.py
# David Prager Branner
# 20140529, works.

import sys
if sys.version_info[0] != 3:
    print('Python 3 required.')
    sys.exit()
import sqlite3
import random
import hsk

"""Using kanji, generate a string for use as the path in a shortened URL."""

def shorten(session, db='url.db'):
    """Return a unique string to represent input string url."""
    # Don't generate new path if one already exists.
    if 'path' in session and session['path']:
        return session['path']
    # New path needed.
    connection = sqlite3.connect(db)
    with connection:
        cursor = connection.cursor()
        path = assign_path(cursor, session['url'])
    return 'http://127.0.0.1:5000/' + path

def assign_path(cursor, url, charset=hsk.simp):
    """Try 20 times to get, at random, an empty slot for a one-digit path.

    If that fails, try two digits, etc."""
    prospective_shortened = None
    n = 1
    while prospective_shortened == None:
        for i in range(20):
            prospective_shortened = ''.join(
                     [random.choice(charset) for i in range(n)])
            # Try to insert; IntegrityError means it already exists in the db.
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
