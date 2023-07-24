#!/usr/bin/python3
"""This module is used to interact with an api"""


import csv
import requests
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    u_id = argv[1]
    api_url = "https://jsonplaceholder.typicode.com"
    url = f"{api_url}/users/{u_id}"
    users = requests.get(url).json()
    user = users["name"]
    tasks = requests.get(f"{api_url}/todos").json()
    tasks_for_id = []

    for key in tasks:
        if key["userId"] == u_id:
            tasks_for_id.append(key)

    u_name = users["username"]
    file_name = f"{u_id}.csv"

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for key in tasks_for_id:
            writer.writerow([str(u_id), users["username"],
                str(key["completed"]), key["title"]])
