#!/usr/bin/python3
""" Gather data from an API """
import json
import requests
from sys import argv


def request_api():
    """Gather data from an API"""
    user = "https://jsonplaceholder.typicode.com/todos/"
    var = 1

    for count in user:
        todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(var)
        user1 = "https://jsonplaceholder.typicode.com/users/" + str(var)
        response_user = requests.get(user1)
        user_json = response_user.json()
        name_user = user_json.get("username")
        response_todo = requests.get(todo)
        json_t = response_todo.json()
        dict = {}
        list_json = []
        if (name_user is None):
            return
        for index in json_t:
            my_dic = {'username': name_user, 'task': '', 'completed': None}
            task_title = index.get('title')
            true_false = index.get('completed')
            my_dic.update(task=task_title, completed=true_false)
            list_json.append(my_dic)
        dict.update({str(var): list_json})
        with open("todo_all_employees.json", "a") as file:
            json.dump(dict, file)
        var = var + 1


if __name__ == "__main__":
    request_api()
