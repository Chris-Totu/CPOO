# 1. Ecrire un programme qui permet de lire le fichier csv (localite.csv) et stocker les informations.
# 2. Permettre à un utilisateur de rechercher le nom d’une localité sur base du code postal fourni.
# 3. Le programme devra dire quel est le top 4 des localités les plus recherchés.

# -> DEMANDER POUR LE add_locality() SI CEST LA BONNE METHODE ET COMMENT FAIRE SI LE FICHIER N'A PAS DE \n AU PREALABLE PCQ SI Y A PAS CA CONCATENE AVEC LA DERNIERE LIGNE
# -> DEMANDER POUR LE top4_frequent_localities_research() POURQUOI IL NY A QUE LA PREMIERE VILLE QUI S AJOUTE DANS LA LISTE 

import os 
import csv
from collections import Counter

def display_file():
    file_path = os.getcwd() # récupérer le chemin absolu du répertoire de travail courant
    file_path += "/les_fichiers_python/fichiers_csv/exo_1/locality.csv" # Obtenir le chemin du fichier
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            print(f"Nom Ville : {row['name']}\t| ID : {row['id']} | CODE LOCALITE : {row['locality_code']} | CODE CITEE : {row['city_code']} | ZIP : {row['zip']} | ID PAYS : {row['country_id']}")
            line_count += 1
        print(f'{line_count} lignes affichées')

def add_locality():
    file_path = os.getcwd() # récupérer le chemin absolu du répertoire de travail courant
    file_path += "/les_fichiers_python/fichiers_csv/exo_1/locality.csv" # Obtenir le chemin du fichier
    
    name = input('Entrez nom de la localité : ')
    id = input('Entrez id de la localité : ')
    locality_code = input('Entrez code localité de la localité : ')
    city_code = input('Entrez code de la localité : ')
    zip = input('Entrez zip de la localité : ')
    country_id = input('Entrez id pays de la localité : ')
    locality = [id, locality_code, city_code, zip, name, country_id]

    with open(file_path, 'a', newline='') as csv_file: # a+ pour ecrire à la fin du fichier et lire à partir du début
        csv_file.seek(0, 2) #positionne le curseur à la fin du fichier
        writer = csv.writer(csv_file) #création d'un objet writer pour écrire dans le fichier
        writer.writerow(locality) #ajout de la ligne

# Renvoie le nom de la localité si le code est présent, sinon "Aucune localité trouvée avec le code postal xxxx"
def search_locality_code():
    file_path = os.getcwd() # récupérer le chemin absolu du répertoire de travail courant
    file_path += "/les_fichiers_python/fichiers_csv/exo_1/locality.csv" # Obtenir le chemin du fichier

    locality_code = input('Entrez code localité à rechercher : ')  
    add_research_locality(locality_code) #ajout de la recherche dans le fichier "localities_research.csv"  
    
    with open(file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            if line['locality_code'] == locality_code:
                return line['name']
    return "Aucune localité trouvée avec le code postal {}".format(locality_code)

def add_research_locality(locality_code):
    file_path = os.getcwd()
    file_path += "/les_fichiers_python/fichiers_csv/exo_1/localities_research.csv"
    with open(file_path, 'a', newline='') as csv_file: 
        csv_file.seek(0, 2) 
        writer = csv.writer(csv_file) 
        writer.writerow([locality_code])

def top4_frequent_localities_research():
    ## trouver le top 4 des localités ##
    localities_research_path = os.getcwd()
    localities_research_path += "/les_fichiers_python/fichiers_csv/exo_1/localities_research.csv"
    with open(localities_research_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        lines = [line[0] for line in reader] #lire tout les lignes et les stocker dans une liste.
    
    counter = Counter(lines) #compter le nombre d'occurence dans la liste.
    top_4 = [x[0] for x in counter.most_common(4)] #obtenir une liste des 4 codes les plus présent.
    ## Afficher les 4 villes les plus recherchées ##
    locality_path = os.getcwd()
    locality_path += "/les_fichiers_python/fichiers_csv/exo_1/locality.csv"

    localities_list_name_top4 = []
    with open(locality_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            if line['locality_code'] in top_4:                 #si le code est dans le top4
                localities_list_name_top4.append(line['name']) #on rajoute le nom de la ville dans la liste

    return localities_list_name_top4
                


def main():
    display_file()
    #add_locality()
    
    # 5 recherche de localité :
    # for i in range (5):
    #     print(search_locality_code())
    print(top4_frequent_localities_research())

if __name__ == "__main__":
    main()