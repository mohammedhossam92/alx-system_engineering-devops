#!/usr/bin/python3
"""module to get subscribers"""
import requests

def number_of_subscribers(subreddit):
    # Set the custom User-Agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Construct the URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the request was successful, process the JSON data
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If the subreddit is invalid or the request fails, return 0
            return 0

    except requests.RequestException:
        # Handle any request exceptions (network issues, etc.)
        return 0
