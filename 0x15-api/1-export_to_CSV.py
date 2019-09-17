#!/usr/bin/python3
"""Gather data from an API and export to csv"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Python script that, using this REST API, for a given employee ID, returns
       information about his/her TODO list progress."""

    u_id = argv[1]
    user_request = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(u_id)).json()
    name = user_request.get('name')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(u_id)).json()

    with open("{}.csv".format(u_id), mode='w') as file:
        e_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo:
            e_writer.writerow([u_id, name, task.get('completed'),
                              task.get('title')])
