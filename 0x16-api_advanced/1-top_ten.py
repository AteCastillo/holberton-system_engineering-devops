#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first
 10 hot posts listed for a given subreddit.
"""

import requests
import json


def top_ten(subreddit):
    """new"""
    url = 'https://www.reddit.com'
    url_api = '{}/r/{}/hot.json'.format(url, subreddit)
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(url_api, headers=headers)
    values = response.json()
    if response.status_code == 200:
        for i in range(10):
            print(values['data']['children'][i]['data']['title'])
    else:
        return None
