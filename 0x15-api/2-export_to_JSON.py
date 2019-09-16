#!/usr/bin/python3
"""Gather data from an API"""

import urllib
import requests
from sys import argv
import json


if __name__ == "__main__":
    """Python script that, using this REST API, for a given employee ID, returns
       information about his/her TODO list progress."""

    u_id = argv[1]
    user_request = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(u_id)).json()
    name = user_request.get('name')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    json_f = {}
    tasks = []
    for task in todo:
        dic = {"task": task.get('title'), "completed": task.get('completed'),
               "username": name}
        tasks.append(dic)
        json_f[u_id] = tasks
    with open("{}.json".format(u_id), mode='w') as file:
        json.dump(json_f, file)
