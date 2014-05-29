#!/usr/bin/env python3
# utils.py
# David Prager Branner
# 20140529, works

"""Utilities for URL-Shortener project."""

import urllib.request as R

def validate_by_opening(url):
    """Try opening a URL and report whether successful or not."""
    try:
        code = R.urlopen(url).getcode()
    except ValueError as e:
        return
    if code == 200:
        return True
