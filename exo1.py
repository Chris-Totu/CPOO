"""
Exo 1
-----

Programme qui demande à l'utilisateur son nom, son prénom et son âge et lui affiche la câtégorie d'âge auquel il appartient.
9 -> 10 ans: Poussin,
11 -> 12 ans: Benjamin,
13 -> 14 ans: Minime,
15 -> 16 ans: Cadet,
17 -> 18 ans: Junior,
19 -> 34 ans: Senior,
35 -> 99 ans: Veteran.

+ tester 50 fois cette fonction
"""

import random


# # Premiere version
# def categoryAge(age):
#     if age >= 9 and age < 11:
#         return 'Poussin'
#     elif age >= 11 and age <= 12:
#         return 'Benjamin'
#     elif age >= 13 and age <= 14:
#         return 'Minime'
#     elif age >= 15 and age <= 16:
#         return 'Cadet'
#     elif age >= 17 and age <= 18:
#         return 'Junior'
#     elif age >= 19 and age <= 34:
#         return 'Senior'
#     elif age > 34:
#         return 'Veteran'
#     else : 
#         return "Aucune catégorie pour votre age."


# Deuxieme version plus optimisée ?
def categoryAge(age):
    categories = {
        (9, 10): 'Poussin',
        (11, 12): 'Benjamin',
        (13, 14): 'Minime',
        (15, 16): 'Cadet',
        (17, 18): 'Junior',
        (19, 34): 'Senior',
        (35, 99): 'Veteran'
    }

    for age_range, category in categories.items():
        if age_range[0] <= age <= age_range[1]:
            return category


# Obtention de l'age de l'utilisateur compris entre 9 et 99 ans
def getAgeUser():
    while True:
        try:
            age = int(input('Entrez votre âge (doit etre un entier compris entre 9 et 99 ans) : '))
            if age > 8 and age < 100:
                return age
            else:
                print('L\'age doit etre compris entre 9 et 99 ans.')

        except ValueError:
            print('Votre age n\'est pas un nombre valide !\n')


# Obtention du nom de l'utilisateur
def getName():
    return input('Entrez votre nom : ')


# Obtention du prénom de l'utilisateur
def getFirstName():
    return input('Entrez votre prénom : ')


# Affichage nom + prenom et catégorie de la personne
def diplayPersonne(name, fistName, age):
    print(f'{name} {firstName}, à {age} ans, vous etes \'{categoryAge(age)}\'.')


#Tester la fonction categoryAge() 50 fois :
print('TEST FONCTION categroyAge() 50x :\n')
for i in range(50):
    age = random.randint(9, 99)
    print(f'A {age} an(s), vous etes : {categoryAge(age)}')


name = getName()
firstName = getFirstName()
age = getAgeUser()
diplayPersonne(name, firstName, age)