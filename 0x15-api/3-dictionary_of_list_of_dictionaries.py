#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """Python script that, using this REST API, for a given employee ID, returns
       information about his/her TODO list progress."""

    user_request = requests.get("https://jsonplaceholder.typicode.com/users")
    user_request = user_request.json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    json_f = {}
    for u_req in user_request:
        u_id = u_req.get('id')
        name = u_req.get('username')
        tasks = []
        for task in todo:
            if task.get('userId') == u_id:
                dic = {"username": name, "task": task.get('title'),
                       "completed": task.get('completed')}
                tasks.append(dic)
        json_f[u_id] = tasks
    with open("todo_all_employees.json", mode='w') as file:
        json.dump(json_f, file)
