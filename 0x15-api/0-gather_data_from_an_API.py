#!/usr/bin/python3
"""
Testing employee data from API
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_request = requests.get(
                f"{REST_API}users/{user_id}"
            ).json()
            todos_request = requests.get(
                f"{REST_API}todos"
            ).json()
            employee_name = user_request.get('name')
            tasks = list(
                filter(lambda x: x.get('userId') == user_id, todos_request)
            )
            completed_tasks = list(
                filter(lambda x: x.get('completed'), tasks)
            )
            print(
                f"Employee {employee_name} is done with tasks"
                f"({len(completed_tasks)}/{len(tasks)}):"
            )
            if completed_tasks:
                for task in completed_tasks:
                    print(f"\t {task.get('title')}")
