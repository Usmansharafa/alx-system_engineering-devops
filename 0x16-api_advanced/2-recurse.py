#!/usr/bin/python3
"""This is a module that implements the recursive function that returns a list
of hot posts in a subreddit"""


def recurse(subreddit, hot_list=[], after=None, count=0):
    """This function returns the list of hot posts in a subreddit using
    recursive calls"""

    import requests
    headers = {'User-Agent': "Ackermannn's bot"}
    base_url = "https://www.reddit.com"
    endpoint = f'r/{subreddit}/hot.json'

    response = requests.get(f'{base_url}/{endpoint}', headers=headers,
                            params={'after': after, 'count': count},
                            allow_redirects=False)

    if response.status_code >= 400:
        print("None")

    info = response.json()
    hotlist = hot_list + [child.get('data').get('title')
                          for child in info.get('data').get('children')]
    if not info.get('data').get('after'):
        return hotlist
    return (recurse(subreddit, hotlist, info.get('data').get('after'),
            info.get('data').get('count')))
