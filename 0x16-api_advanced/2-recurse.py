#!/usr/bin/python3
"""
Recursive function to retrieve hot article titles from a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit.
    If the subreddit is invalid, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": (
            "0x016-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
        )
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    # Check for invalid subreddit
    if response.status_code == 404:
        return None

    # Parse response data
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist", 0)

    # Add titles to the hot_list
    hot_list.extend(
        child.get("data", {}).get("title")
        for child in results.get("children", [])
    )

    # If there are more pages, recurse
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
