#!/usr/bin/python3
"""This module is used to interact with an api"""


import requests
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    u_id = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com"
    url = f"{api_url}/users/{u_id}"
    users = requests.get(url).json()
    user = users["name"]
    tasks = requests.get(f"{api_url}/todos").json()
    tasks_for_id = []

    for key in tasks:
        if key["userId"] == u_id:
            tasks_for_id.append(key)

    completed_tasks = []

    for key in tasks_for_id:
        if key["completed"]:
            completed_tasks.append(key)

    total_tasks = len(tasks_for_id)
    completed = len(completed_tasks)
    print(f"Employee {user} is done with tasks({completed}/{total_tasks}):")
    for key in completed_tasks:
        print(f"\t {key['title']}")
