#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'user agent'
    }
    try:
        res = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers=headers, allow_redirects=False
        )
        if res.status_code == 200:
            json_res = res.json()
            data_dict = json_res.get('data')
            if data_dict:
                return data_dict.get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0
