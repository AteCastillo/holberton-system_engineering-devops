#!/usr/bin/python3
"""
returns the number of subscribers for a given subredit
"""

import requests


def number_of_subscribers(subreddit):
    """new"""
    url_api = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:88.0)\
                            Gecko/20100101 Firefox/88.0'}
    response = requests.get(url_api, headers=headers)
    if response.status_code == 200:
        return (response.json().get('data').get('subscribers'))
    else:
        return 0
