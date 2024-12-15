#!/usr/bin/python3
"""
Query the number of subscribers for a subreddit.
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if an error occurs.
    """
    user_agent = {'User-Agent': 'lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=user_agent).json()
        return response.get('data', {}).get('subscribers', 0)
    except Exception:
        return 0


if __name__ == "__main__":
    if len(argv) > 1:
        print(number_of_subscribers(argv[1]))
    else:
        print(0)
