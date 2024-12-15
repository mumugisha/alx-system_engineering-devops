#!/usr/bin/python3
"""
Fetch employee data from the API and display their task progress.
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Validate that the argument is a positive integer (employee ID)
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])

            # Fetch user details
            user = requests.get(f"{REST_API}users/{user_id}").json()
            if not user:
                print("Employee not found")
                sys.exit(1)

            # Fetch tasks for the user
            tasks = requests.get(f"{REST_API}todos").json()
            user_tasks = [
                task for task in tasks if task["userId"] == user_id
            ]

            # Separate completed tasks
            completed_tasks = [
                task for task in user_tasks if task["completed"]
            ]

            # Display user name and task completion stats
            employee_name = user.get("name")
            print(
                f"Employee {employee_name} is done with tasks("
                f"{len(completed_tasks)}/{len(user_tasks)}):"
            )

            # Display each completed task title
            for task in completed_tasks:
                print(f"\t {task.get('title')}")
