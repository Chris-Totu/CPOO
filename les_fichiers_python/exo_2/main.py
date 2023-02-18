### Ecrire un programme qui permet à une personne d’enregistrer son nom, son prénom et sa profession.
# Le programme lui dit alors s’il est présent dans le fichier.
# S’il n’est pas présent, on le mets dans le fichier.
# S’il est présent, on lui demande s’il veut modifier
# ces données (Si oui, on l’invite alors à encoder ses nouvelles données) ou supprimer ces données.

import os
from ast import literal_eval #convertir une chaîne de caractères qui représente un objet Python, tel qu'un dictionnaire ou une liste, en l'objet Python correspondant. 

def register():
    ### Demande les datas de la personne et return un dictionnaire sous forme d'un string ###
    person = {'first_name' : '', 'last_name' : '', 'profession' : ''}
    person['first_name'] = input("Entrez votre nom : ")
    person['last_name'] = input("Entrez votre prénom : ")
    person['profession'] = input("Entrez votre profession : ")

    return str(person)

def add_in_file(person):
    ### Ajoute une ligne des datas d'une personne dans le fichiers data.txt  ###
    current = os.getcwd()
    current += "/CPOO/les_fichiers_python/exo_2/data.txt"
    
    with open(current, 'a') as f:
        f.write(person + '\n') # \n pour qu'à la prochaine écriture ca aille à la ligne

def is_present_in_file(person):
    isPresent = False
    current = os.getcwd()
    current += "/CPOO/les_fichiers_python/exo_2/data.txt"
    person = literal_eval(person) #retourner le dictionnaire qui etait passé en string
    
    with open(current, 'r') as f:
        for line in f:
            person_data = literal_eval(line)
            if (person_data['first_name'] == person['first_name'] and
            person_data['last_name'] == person['last_name'] and
            person_data['profession'] == person['profession']):
                isPresent = True
                break

    return isPresent

def change_date():
    pass

def main():
    person = register()
    #add_in_file(person)
    print(is_present_in_file(person))

if __name__ == "__main__":
    main()