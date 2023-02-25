### Ecrire un programme qui permet à une personne d’enregistrer son nom, son prénom et sa profession.
# Le programme lui dit alors s’il est présent dans le fichier.
# S’il n’est pas présent, on le mets dans le fichier.
# S’il est présent, on lui demande s’il veut modifier
# ces données (Si oui, on l’invite alors à encoder ses nouvelles données) ou supprimer ces données.

import os
from ast import literal_eval #convertir une chaîne de caractères qui représente un objet Python, tel qu'un dictionnaire ou une liste, en l'objet Python correspondant. 
import pdb
DELETE = True
REWRITE = False

# Demande les datas de la personne et return un dictionnaire sous forme d'un string
def register():
    person = {'first_name' : '', 'last_name' : '', 'profession' : ''}
    person['first_name'] = input("Entrez votre nom : ")
    person['last_name'] = input("Entrez votre prénom : ")
    person['profession'] = input("Entrez votre profession : ")

    return str(person)

# Ajoute les datas d'une personne dans le fichiers data.txt
def add_in_file(person):
    current = os.getcwd()
    current += "/les_fichiers_python/exo_2/data.txt"
    with open(current, 'a') as f:
        f.write(person + '\n') # \n pour qu'à la prochaine écriture ca aille à la ligne

# Renvoie true si la personne est présente dans le fichiers, false sinon
def is_present(person):
    
    isPresent = False
    current = os.getcwd()
    current += "/les_fichiers_python/exo_2/data.txt"
    person = literal_eval(person) #converti le string des datas en dictionnaire
    
    with open(current, 'r') as f:
        for line in f:
            person_data = literal_eval(line)
            if (person_data['first_name'] == person['first_name'] and
            person_data['last_name'] == person['last_name'] and
            person_data['profession'] == person['profession']):
                isPresent = True
                break

    return isPresent

#Fonction qui demande à l'utilisateur si il veut changer ses données
# Renvoie false si l'utilisateur ne veut rien faire
# Renvoie true si l'utilisateur veut réencoder ses données
# Renvoie -1 si l'utilisateur veut supprimer ses données
def ask_change_data():
    while True:
        choice = input("Voulez-vous changer vos données ? (changer/supprimer/rien) ").lower()
        if choice == "changer":
            return False
        elif choice == "rien":
            return -1
        elif choice == "supprimer":
            return True
        else:
            print("Votre choix est incorrect. Veuillez entrer 'changer', 'supprimer' ou 'rien'.")
            continue

# Supprime la personne des datas
def delete_person(person):
    current = os.getcwd()
    current += "/les_fichiers_python/exo_2/data.txt"
    person = literal_eval(person)

    with open(current, 'r') as f:
        lines = f.readlines()

    with open(current, 'w') as f:
        for line in lines:
            person_data = literal_eval(line)
            if (person_data['first_name'] == person['first_name'] and
            person_data['last_name'] == person['last_name'] and
            person_data['profession'] == person['profession']):
                continue
            f.write(line)
    
    print("Vous avez été supprimé du fichier.")

# Demande les nouvelles données d'une personne et les remplaces dans le fichier    
def change_data(person):
    current = os.getcwd()
    current += "/les_fichiers_python/exo_2/data.txt"
    person = literal_eval(person)
    updated_person = register() # demande les nouvelles données de la personne
    updated_person = literal_eval(updated_person) # converti le string des nouvelles données en dictionnaire

    with open(current, 'r') as f:
        lines = f.readlines()

    with open(current, 'w') as f:
        for line in lines:
            person_data = literal_eval(line)
            if (person_data['first_name'] == person['first_name'] and
            person_data['last_name'] == person['last_name'] and
            person_data['profession'] == person['profession']):
                f.write(str(updated_person) + '\n') # écrit les nouvelles données
            else:
                f.write(line) # réécrit la ligne telle qu'elle était avant

def main():
    person = register()
    if is_present(person):
        print('Vous êtes encodé dans le fichier.')
        choice = ask_change_data()
        if choice == DELETE:
            delete_person(person)
        elif choice == REWRITE:
            change_data(person)
        else:
            print("Aucun changement.\nFin de programme.")
    else: 
        add_in_file(person)
        print("Vous n'etiez pas encodé dans le fichier. Vous êtes maintenant encodé dans le fichier.")
        print("Fin de programme.")

if __name__ == "__main__":
    main()