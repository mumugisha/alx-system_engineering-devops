#!/usr/bin/python3
"""
Fetch employee data from the API and display their task progress.
"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    users_dictionary = {}
    for user in users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            USER_ID)
        todos_url = user_url + '/todos/'
        response = requests.get(todos_url)

        user_tasks = response.json()
        users_dictionary[USER_ID] = []
        for task in user_tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dictionary[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })

    # Export to JSON
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dictionary, f)
