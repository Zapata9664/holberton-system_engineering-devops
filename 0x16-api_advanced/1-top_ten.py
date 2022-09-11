#!/usr/bin/python3
"""Returns the number of subscribers
(not active users, total subscribers) for a given subreddit."""
import json
import requests


def top_ten(subreddit):
    """Number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "reddit_user"}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        print('None')
    else:
        data = request.json()["data"]
        list2 = data["children"]

        for post in list2[0:10]:
            print(post["data"]["title"])
