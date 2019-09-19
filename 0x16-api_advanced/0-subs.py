#!/usr/bin/python3
"""How many subs?"""

import json
import requests


def number_of_subscribers(subreddit):
    """function that queries Reddit API and returns the number of subscribers"""

    headers = {"User-Agent": "Holberton-User"}
    request_url = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit),
                           headers=headers,
                           allow_redirects=False)

    if request_url.status_code >= 300:
        return (0)

    request_url = request_url.json()

    if "data" in request_url:
        return (request_url.get("data").get("subscribers"))
    else:
        return (0)
