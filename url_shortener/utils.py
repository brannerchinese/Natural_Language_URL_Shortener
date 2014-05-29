#!/usr/bin/env python3
# utils.py
# David Prager Branner
# 20140529, works

"""Utilities for URL-Shortener project."""

import urllib.request
import urllib.parse

def validate_by_opening(url):
    """Try opening a URL and report whether successful or not."""
    print(repr(url))
#    url = urllib.parse.quote(url, safe='/:')
    url = url.strip('\n\r')
    print(repr(url))
    try:
        code = urllib.request.urlopen(url).getcode()
    except Exception as e:
        return False
    if code == 200:
        return True
