#! /usr/bin/env python
# shorten.py
# David Prager Branner
# 20140527

import hashlib

def shorten(s):
    """Return a unique string to represent input string s."""
    # Idea: since the purpose of shortening is for human convenience, use
    # random strings of Chinese characters rather than ASCII.
    #
    # Input string s => hash
    # hash: random kanji assignment (stored in database)
    pass
