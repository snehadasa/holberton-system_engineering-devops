#!/usr/bin/python3
"""Gather data from an API"""

import urllib
import requests
from sys import argv
import json


if __name__=="__main__":
    """Python script that, using this REST API, for a given employee ID, returns
       information about his/her TODO list progress."""

    u_id = argv[1]
    user_request = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(u_id)).json()
    name = user_request.get('name')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    total = 0
    completed = 0
    tasks = []
    for task in todo:
        if task.get('userId') == u_id:
            total += 1
        if task.get('completed'):
            completed += 1
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))

    for task in tasks:
        print("\t {}".format(task))
