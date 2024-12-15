#!/usr/bin/python3
"""
Exporting API data to a CSV file
"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user_request = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url_user_request)

    # Check if user exists
    if response.status_code != 200:
        print(f"Error: User with ID {user_id} not found.")
        sys.exit(1)

    # Extracting user data
    user_name = response.json().get('username')
    user_tasks_url = f"{url_user_request}/todos"
    response = requests.get(user_tasks_url)
    user_tasks = response.json()

    # Exporting data to CSV
    file_name = f"{user_id}.csv"
    with open(file_name, 'w') as csvfile:
        for task in user_tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write(
                f'"{user_id}","{user_name}","{completed}","{title_task}"\n'
            )
