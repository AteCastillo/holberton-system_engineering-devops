#!/usr/bin/python3
"""
returns the number of subscribers for a given subredit
"""

import requests
import json


def number_of_subscribers(subreddit):
    """new"""
    url = 'https://www.reddit.com'
    url_api = '{}/r/{}/about.json'.format(url, subreddit)
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(url_api, headers=headers)
    subscribers = response.json().get('data').get('subscribers')
    if response.status_code == 200:
        return subscribers
    else:
        return 0
