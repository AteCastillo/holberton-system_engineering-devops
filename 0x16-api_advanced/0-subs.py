#!/usr/bin/python3
"""
returns the number of subscribers for a given subredit
"""

import requests


def number_of_subscribers(subreddit):
    """new"""
    if (type(subreddit) is not str):
        return(0)
    url = 'https://www.reddit.com'
    url_api = '{}/r/{}/about.json'.format(url, subreddit)
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:88.0)\
                            Gecko/20100101 Firefox/88.0'}
    response = requests.get(url_api, headers=headers)
    subscribers = response.json().get('data').get('subscribers')
    if response.status_code == 200:
        return subscribers
    else:
        return 0
