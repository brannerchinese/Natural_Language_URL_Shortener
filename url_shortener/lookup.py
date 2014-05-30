#!/usr/bin/env python3
# lookup.py
# David Prager Branner
# 20140530, works.

"""Retrieve a URL from the database."""

from sqlalchemy import create_engine, MetaData, Table

def get_url(path, db='url.db'):
    """Retreive URL corresponding to a given path."""
    engine = create_engine('sqlite:///url.db')
    metadata = MetaData(bind=engine)
    users = Table('shortened_to_url', metadata, autoload=True)
    url = users.select(users.c.shortened == path).execute().first()
    try:
        url = url[1]
    except Exception:
        url = None
    return url
