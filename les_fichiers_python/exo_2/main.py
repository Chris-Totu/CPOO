### Ecrire un programme qui permet à une personne d’enregistrer son nom, son prénom et sa profession.
# Le programme lui dit alors s’il est présent dans le fichier.
# S’il n’est pas présent, on le mets dans le fichier.
# S’il est présent, on lui demande s’il veut modifier
# ces données (Si oui, on l’invite alors à encoder ses nouvelles données) ou supprimer ces données.

import os

def register():
    person = {'first_name' : '', 'last_name' : '', 'profession' : ''}
    person['first_name'] = input("Entrez votre nom : ")
    person['last_name'] = input("Entrez votre prénom : ")
    person['profession'] = input("Entrez votre profession : ")

    return person

def add_in_file(person):
    


def is_present_in_file(person):



def main():
    pass

if __name__ == "__main__":
    main()