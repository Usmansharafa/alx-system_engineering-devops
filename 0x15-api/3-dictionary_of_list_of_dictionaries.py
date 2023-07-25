#!/usr/bin/python3
"""This module is used to interact with an api"""


import json
import requests


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    url = f"{api_url}/users/"
    users = requests.get(url).json()
    tasks = requests.get(f"{api_url}/todos").json()
    u_names = [key["username"] for key in users]
    u_ids = [key["id"] for key in users]
    new_dict = {}
    for u_id in u_ids:
        tasks_for_id = [key for key in tasks if key["userId"] == u_id]
        for keys in tasks_for_id:
            keys["task"] = keys["title"]
            keys["username"] = u_names[u_id - 1]
            del keys["id"]
            del keys["title"]
        new_dict[str(u_id)] = tasks_for_id
    for keys, values in new_dict.items():
        for key in values:
            del key["userId"]

    with open("todo_all_employees.json", "w") as json_f:
        json.dump(new_dict, json_f)
