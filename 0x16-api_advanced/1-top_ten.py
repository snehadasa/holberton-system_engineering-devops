#!/usr/bin/python3
"""Top ten"""

import json
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the first
       10 hot posts listed for a given subreddit"""

    headers = {"User-Agent": "Holberton-User"}
    request_url = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                               .format(subreddit),
                               headers=headers,
                               allow_redirects=False)

    if request_url.status_code >= 300:
        print(None)
        return

    request_url = request_url.json()

    if "data" in request_url:
        for children_title in request_url.get("data").get("children"):
            print(children_title.get("data").get("title"))
    else:
        print(None)
        return
