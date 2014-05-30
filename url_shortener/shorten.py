#! /usr/bin/env python
# shorten.py
# David Prager Branner
# 20140530, works.

import sys
if sys.version_info[0] != 3:
    print('Python 3 required.')
    sys.exit()
from sqlalchemy import create_engine, MetaData, Table
import random
import hsk

"""Using kanji, generate a string for use as the path in a shortened URL."""

def shorten(session, db='url.db'):
    """Return a unique string to represent input string url."""
    # Don't generate new path if one already exists.
    if 'path' in session and session['path']:
        return session['path']
    # New path needed.
    path = assign_path(session['url'])
    return 'http://127.0.0.1:5000/' + path

def assign_path(url, charset=hsk.simp):
    """Try 20 times to get, at random, an empty slot for a one-digit path.

    If that fails, try two digits, etc."""
    prospective_shortened = None
    n = 1
    engine = create_engine('sqlite:///url.db')
    connection = engine.connect()
    metadata = MetaData(bind=engine)
    urls = Table('shortened_to_url', metadata, autoload=True)
    while prospective_shortened == None:
        for i in range(20):
            prospective_shortened = ''.join(
                     [random.choice(charset) for i in range(n)])
            # Try to insert; IntegrityError means it already exists in the db.
            try:
                connection.execute(
                        urls.insert(), url=url, shortened=prospective_shortened)
                break
            except Exception as e:
                print(e)
                prospective_shortened = None
                continue
        n += 1
    return prospective_shortened
