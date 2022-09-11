#!/usr/bin/python3
""" Returns information about his/her data list progress. """

import csv
import json
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


    dict = {}
    list_json = []
    for index in todo_json:
        my_dic = {'task': '', 'completed': None, 'username': name_user}
        task_title = index.get('title')
        boolean = index.get('completed')
        my_dic.update(task=task_title, completed=boolean)
        list_json.append(my_dic)
    dict.update({argv[1]: list_json})

    with open(argv[1]+'.'+'json', 'w') as file:
        json.dump(dict, file)


if __name__ == "__main__":
    request_api(argv)

