#!/usr/bin/env python3
# lookup.py
# David Prager Branner
# 20140529, works.

"""Retrieve a URL from the database."""

import sqlite3

def get_url(path, db='url.db'):
    """Retreive URL corresponding to a given path."""
    print('path:', path)
    connection = sqlite3.connect(db)
    retrieved = None
    with connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                    '''SELECT url '''
                    '''FROM shortened_to_url '''
                    '''WHERE shortened=? ''', path
                    )
        except Exception as e:
            print(e)
        url = cursor.fetchone()
    print('in lookup.get_url; url:', url[0]) # debug
    return url[0]
