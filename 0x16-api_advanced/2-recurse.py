#!/usr/bin/python3
"""Returns the number of subscribers
(not active users, total subscribers) for a given subreddit."""
import json
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after:
        url += "?after={}".format(after)
    headers = {"User-Agent": "reddit_user"}
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        return None
    data = request.json()["data"]
    posts = data["children"]
    for post in posts:
        count += 1
        hot_list.append(post["data"]["title"])
    after = data["after"]
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
