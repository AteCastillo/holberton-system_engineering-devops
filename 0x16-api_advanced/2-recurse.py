#!/usr/bin/python3
"""queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit recursively
"""

import requests

def recurse(subreddit, hot_list=[]):
    """new"""
    