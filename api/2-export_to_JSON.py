#!/usr/bin/python3
"""Script to fetch and export employee TODO list progress from a REST API to JSON."""
import json  # Importation de la bibliothèque JSON pour la manipulation des fichiers JSON
import requests  # Importation de la bibliothèque requests pour les requêtes HTTP
import sys  # Importation du module sys pour utiliser les arguments de la ligne de commande

# Vérification du nombre d'arguments passés en ligne de commande
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employeeId(int)")  # Instructions d'utilisation
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

USER_TASK = {EMPLOYEE_ID: []}  # Initialisation d'un dictionnaire pour stocker les tâches de l'employé
for task in data:
    task_dict = {
        "task": task["title"],  # Titre de la tâche
        "completed": task["completed"],  # Statut de la tâche
        "username": task["user"]["username"]  # Nom d'utilisateur de l'employé
    }
    USER_TASK[EMPLOYEE_ID].append(task_dict)  # Ajout de la tâche au dictionnaire

# Écriture des données dans un fichier JSON avec l'identifiant de l'employé comme nom de fichier
with open(f"{EMPLOYEE_ID}.json", "w") as file:
    json.dump(USER_TASK, file)  # Écriture des données dans le fichier JSON
