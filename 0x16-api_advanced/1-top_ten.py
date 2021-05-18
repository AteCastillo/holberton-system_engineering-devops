#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first
 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """new"""
    if (type(subreddit) is not str):
        return(0)
    url = 'https://www.reddit.com'
    url_api = '{}/r/{}/hot.json'.format(url, subreddit)
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:88.0)\
                            Gecko/20100101 Firefox/88.0'}
    response = requests.get(url_api, headers=headers, allow_redirects=False)
    values = response.json()
    if response.status_code == 200:
        for i in range(10):
            print(values['data']['children'][i]['data']['title'])
    else:
        return None
