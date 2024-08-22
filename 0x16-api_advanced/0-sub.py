#!/usr/bin/python3
"""Function"""
import requests


def number_of_subscribers(subreddit):
    """Return"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:subscribers_counter:v1.0.0 (by /u/SubstantialWar264)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
