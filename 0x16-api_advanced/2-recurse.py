#!/usr/bin/python3
"""Recurse it!"""

import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries the Reddit API and returns a list
       containing the titles of all hot articles for a given subreddit. If no
       results are found for the given subreddit, the function should
       return None."""

    headers = {"User-Agent": "Holberton-User"}
    params = {"after": after}
    request_url = requests.get("https://www.reddit.com/r/{}/hot.json"
                               .format(subreddit),
                               params=params,
                               headers=headers,
                               allow_redirects=False)

    if request_url.status_code >= 300:
        return (None)

    request_url = request_url.json()

    if after is None:
        return (hot_list)

    if "data" in request_url:
        for children_title in request_url.get("data").get("children"):
            hot_list.append(children_title.get("data").get("title"))
    else:
        return (None)
    a = request_url.get("data").get("after")
    return recurse(subreddit, hot_list, a)
