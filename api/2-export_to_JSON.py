#!/usr/bin/python3
"""export data from api to JSON file """
import csv
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <integer>")
        sys.exit(1)

    # URL builder
    base = "https://jsonplaceholder.typicode.com"
    users = "users"
    users_url = base + "/" + users
    response = requests.get(users_url)
    employee_info = response.json()

    # specific employee info
    input_id = str(sys.argv[1])
    id_url = base + "/" + users + "/" + input_id
    response = requests.get(id_url)
    employee_info = response.json()

    # employee name
    EMPLOYEE_NAME = employee_info.get('name')

    # employee username
    USERNAME = employee_info.get('username')

    # number of tasks for employee
    todo = "todos"
    task_per_user_url = id_url + "/" + todo
    response = requests.get(task_per_user_url)
    list_of_todos = response.json()
    TOTAL_NUMBER_OF_TASKS = len(list_of_todos)

    # number of tasks completed for employee
    completed_tasks = []
    for todo in list_of_todos:
        if todo.get('completed') is True:
            completed_tasks.append(todo)
    NUMBER_OF_DONE_TASKS = len(completed_tasks)

    # export data of tasks for user_id in JSON format
    task_list = []
    for task in list_of_todos:
        task_info = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': USERNAME
            }
        task_list.append(task_info)
        USER_ID = str(input_id)

    json_dict = {USER_ID: task_list}
    print(json_dict)

    filename = input_id + ".json"
    with open(filename, 'w') as write_file:
        json.dump(json_dict, write_file)
