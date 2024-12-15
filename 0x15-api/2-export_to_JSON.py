#!/usr/bin/python3
"""
Script to import data from an API and export it to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"

    # Fetch user information
    response = requests.get(url_user)
    USERNAME = response.json().get('username')

    # Fetch tasks for the user
    url_user_tasks = f"{url_user}/todos"
    response = requests.get(url_user_tasks)
    users_tasks = response.json()

    # Prepare data for export
    dictionary_data = {USER_ID: []}
    for task in users_tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dictionary_data[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        })

    # Write data to a JSON file
    with open(f"{USER_ID}.json", 'w') as f:
        json.dump(dictionary_data, f)
