#!/usr/bin/python3
"""export data from api to CSV file """
import csv
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

    # export data of tasks for user_id in CSV format
    task_list = []
    for task in list_of_todos:
        task_info = {
            'USER_ID': str(input_id),
            'USERNAME': USERNAME,
            'TASK_COMPLETED_STATUS': task.get('completed'),
            'TASK_TITLE': task.get('title')
            }
        task_list.append(task_info)

    filename = input_id + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        writer.writerows(task_list)
