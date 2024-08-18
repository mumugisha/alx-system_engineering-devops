#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                return data.get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0
