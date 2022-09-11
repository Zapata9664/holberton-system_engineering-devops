#!/usr/bin/python3
""" Returns information about his/her data list progress. """

import csv
import requests
from sys import argv


def request_api(argv):
    """Module for do request api"""
    users = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    response_todo = requests.get(todo)
    response_user = requests.get(users)
    todo_json = response_todo.json()
    user_json = response_user.json()
    name_user = user_json.get("username")

    with open(argv[1]+'.'+'csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for count in todo_json:
            writer.writerow([argv[1], str(name_user),
                            str(count['completed']), str(count['title'])])


if __name__ == "__main__":
    request_api(argv)
