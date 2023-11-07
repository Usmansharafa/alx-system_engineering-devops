#!/usr/bin/python3
"""This is a module that implements the function that lists the hot posts
in a subreddit"""


def top_ten(subreddit):
    """This function prints the list of hot posts in a subreddit"""

    import requests
    headers = {'User-Agent': "Ackermannn's bot"}
    base_url = "https://www.reddit.com"
    endpoint = f'r/{subreddit}/hot.json?limit=10'

    response = requests.get(f'{base_url}/{endpoint}', headers=headers,
                            allow_redirects=False)

    if response.status_code >= 300:
        print("None")
    else:
        data = response.json()
        [print(sub['data']['title']) for sub in data['data']['children']]
