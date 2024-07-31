#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    tasks = [task.get('title') for task in todos if task.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".
          format(user_id.get('name'), len(tasks), len(todos)))

    for task in tasks:
        print("\t {}".format(task))
