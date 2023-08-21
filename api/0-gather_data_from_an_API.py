#!/usr/bin/python3
"""This script retrieves and processes data from the JSONPlaceholder API to
 gather information about an employee's tasks. """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <integer>")
        sys.exit(1)

    # URL builder
    base = "https://jsonplaceholder.typicode.com"
    users = "users"
    employee_id = str(sys.argv[1])
    api_url = base + "/" + users + "/" + employee_id
    response = requests.get(api_url)

    # employee name
    employee_info = response.json()
    EMPLOYEE_NAME = employee_info.get('name')

    # number of tasks for employee
    todo = "todos"
    task_per_user_url = api_url + "/" + todo
    response = requests.get(task_per_user_url)
    list_of_todos = response.json()
    TOTAL_NUMBER_OF_TASKS = len(list_of_todos)

    # number of tasks completed for employee
    completed_tasks = []
    for todo in list_of_todos:
        if todo.get('completed') is True:
            completed_tasks.append(todo)
    NUMBER_OF_DONE_TASKS = len(completed_tasks)

    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}\
/{TOTAL_NUMBER_OF_TASKS}):")

    for task in completed_tasks:
        task_name = task.get('title')
        print(f"\t{task_name}")
