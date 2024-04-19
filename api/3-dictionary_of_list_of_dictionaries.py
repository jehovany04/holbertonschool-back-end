#!/usr/bin/python3
"""Returns info about an employee's TODO list using REST API."""
import json  # Importation de la bibliothèque JSON pour la manipulation des fichiers JSON
import requests  # Importation de la bibliothèque requests pour les requêtes HTTP

# Récupération des informations sur les employés et leurs tâches
if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"  # Lien de base de l'API REST

    # Récupération de la liste des employés
    employees = requests.get(f"{link}/users").json()

    all_employees_tasks = {}  # Initialisation d'un dictionnaire pour stocker les tâches de tous les employés

    # Parcours de chaque employé pour récupérer ses tâches
    for employee in employees:
        employee_id = employee.get("id")  # Identifiant de l'employé
        todo_list = requests.get(f"{link}/todos?userId={employee_id}").json()  # Récupération de la liste des tâches

        # Création d'une liste de dictionnaires contenant les détails de chaque tâche de l'employé
        employee_tasks = [{"username": employee.get("username"),
                           "task": todo.get("title"),
                           "completed": todo.get("completed")}
                          for todo in todo_list]

        all_employees_tasks[employee_id] = employee_tasks  # Stockage des tâches de l'employé dans le dictionnaire

    # Écriture des données dans un fichier JSON
    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_employees_tasks, f)  # Écriture des données dans le fichier JSON
