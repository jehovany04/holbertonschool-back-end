#!/usr/bin/python3
"""Script to fetch and export employee TODO list progress from a REST API to CSV."""
import csv  # Importation de la bibliothèque CSV pour la manipulation des fichiers CSV
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

USERNAME = data[0]["user"]["username"]  # Récupération du nom d'utilisateur de l'employé

# Écriture des données dans un fichier CSV avec l'identifiant de l'employé comme nom de fichier
with open(f"{EMPLOYEE_ID}.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    for task in data:
        writer.writerow(
            [EMPLOYEE_ID, USERNAME, str(task["completed"]), task["title"]]
        )  # Écriture des données de chaque tâche dans le fichier CSV
