#!/usr/bin/python3
"""This module is used to interact with an api"""


import json
import requests
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    u_id = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com"
    url = f"{api_url}/users/{u_id}"
    users = requests.get(url).json()
    tasks = requests.get(f"{api_url}/todos").json()
    tasks_for_id = []

    for key in tasks:
        if key["userId"] == u_id:
            tasks_for_id.append(key)

    for key in tasks_for_id:
        key["task"] = key["title"]
        key["username"] = users["username"]
        del key["title"]
        del key["userId"]
        del key["id"]
    response = {u_id: tasks_for_id}
    file_name = f"{u_id}.json"

    with open(file_name, "w") as json_f:
        json.dump(response, json_f)
