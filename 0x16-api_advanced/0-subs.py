#!/usr/bin/python3
"""This is a module that implements the function that gets the total number
of subcribers to a subreddit"""


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers to a subreddit"""

    import requests
    headers = {'User-Agent': "Ackermannn's bot"}
    base_url = "https://www.reddit.com"
    endpoint = f'r/{subreddit}/about.json'

    response = requests.get(f'{base_url}/{endpoint}', headers=headers,
                            allow_redirects=False)

    if response.status_code >= 300:
        return (0)
    else:
        data = response.json()
        subscriber_count = data['data']['subscribers']
        return (subscriber_count)
