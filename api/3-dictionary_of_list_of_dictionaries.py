#!/usr/bin/python3
"""Returns info about an employee's TODO list using REST API."""
import json
import requests

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"

    employees = requests.get(f"{link}/users").json()

    all_employees_tasks = {}

    for employee in employees:
        employee_id = employee.get("id")
        todo_list = requests.get(f"{link}/todos?userId={employee_id}").json()

        employee_tasks = [{"username": employee.get("username"),
                           "task": todo.get("title"),
                           "completed": todo.get("completed")}
                          for todo in todo_list]

        all_employees_tasks[employee_id] = employee_tasks

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_employees_tasks, f)
