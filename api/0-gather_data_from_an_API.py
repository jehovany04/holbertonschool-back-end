#!/usr/bin/python3
"""Fetch and display TODO list progress for an employee using a REST API."""
import requests  # Importation de la bibliothèque requests pour les requêtes HTTP
import sys  # Importation du module sys pour utiliser les arguments de la ligne de commande

# Vérification du nombre d'arguments passés en ligne de commande
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} employee_id(int)")  # Instructions d'utilisation
        sys.exit(1)  # Sortie du programme avec un code d'erreur

# URL de base pour l'API REST et récupération de l'identifiant de l'employé à partir des arguments
URL = "https://jsonplaceholder.typicode.com"
EMPLOYEE_ID = sys.argv[1]

# Requête GET pour récupérer les tâches de l'employé spécifié
RESPONSE = requests.get(
    f"{URL}/users/{EMPLOYEE_ID}/todos",
    params={"_expand": "user"}
)
data = RESPONSE.json()  # Conversion de la réponse en format JSON

# Vérification de la présence de données dans la réponse
if not len(data):
    print("RequestError:", 404)  # Affichage d'une erreur si aucune donnée n'est trouvée
    sys.exit(1)  # Sortie du programme avec un code d'erreur

# Filtrage des tâches complétées et calcul du nombre total de tâches
TASK_TITLE = [task["title"] for task in data if task["completed"]]
TOTAL_NUMBER_OF_TASKS = len(data)
NUMBER_OF_DONE_TASKS = len(TASK_TITLE)
EMPLOYEE_NAME = data[0]["user"]["name"]  # Récupération du nom de l'employé

# Affichage du progrès de la liste des tâches
print(f"Employee {EMPLOYEE_NAME} is done with tasks"
      f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
for title in TASK_TITLE:
    print("\t ", title)  # Affichage du titre des tâches complétées

