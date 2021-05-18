#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first
 10 hot posts listed for a given subreddit.
"""

import requests
import json


def top_ten(subreddit):
    """new"""
    if (type(subreddit) is not str):
        return(0)
    url_api = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(url_api, headers=headers)
    if response.status_code is not 200:
        return(0)
    return(response.json().get("data").get("subscribers"))
