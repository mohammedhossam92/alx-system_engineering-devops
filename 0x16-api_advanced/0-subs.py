#!/usr/bin/python3
"""
    Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': '0-sub/1.0 (by /u/SubstantialWar265)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0

        data = response.json().get("data")
        if not data:
            return 0

        num_subs = data.get("subscribers", 0)
        return num_subs

    except requests.RequestException:
        # In case of network errors or other request exceptions, return 0
        return 0
