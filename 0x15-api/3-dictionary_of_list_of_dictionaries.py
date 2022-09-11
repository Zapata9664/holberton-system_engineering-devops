#!/usr/bin/python3
""" Returns information about his/her data list progress. """

from requests import get
from json import dump

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    dict_complete = {}
    for usr in users:
        user_id = usr.get('id')
        username = usr.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos'
        response = get(url)
        tasks = response.json()
        dict_complete[user_id] = []
        for task in tasks:
            dict_complete[user_id].append({
                            "task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": username
                            })
    with open('todo_all_employees.json', 'w') as f:
        dump(dict_complete, f)
