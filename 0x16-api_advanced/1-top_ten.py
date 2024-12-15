#!/usr/bin/python3
"""
Top ten number of subscribers
"""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    user_agent = {'User-Agent': 'lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    try:
        response = requests.get(url, headers=user_agent, timeout=10)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print(None)
