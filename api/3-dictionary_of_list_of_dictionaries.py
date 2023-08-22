#!/usr/bin/python3
"""export data from api to JSON file """
import csv
import json
import requests
import sys

if __name__ == "__main__":

    # URL builder
    base = "https://jsonplaceholder.typicode.com"
    users = "users"
    users_url = base + "/" + users
    response = requests.get(users_url)
    employee_info = response.json()

    todo_dict = {}
    for employee in employee_info:
        user_id = str(employee.get('id'))
        username = employee.get('username')
        todos = "todos"
        todo_url = users_url + "/" + user_id + "/" + todos
        response = requests.get(todo_url)
        todo_list = response.json()

        task_list = []
        for task in todo_list:
            task_info = {
                'username': username,
                'task': task.get('title'),
                'completed': task.get('completed')
            }
            task_list.append(task_info)
            todo_dict[user_id] = task_list

            with open("todo_all_employees.json", 'w') as write_file:
                json.dump(todo_dict, write_file)
