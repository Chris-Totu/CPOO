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
         

#Tester la fonction categoryAge() 50 fois :
i = 0
while i < 50:
    age = random.randint(0, 100)
    print(f'A {age} an(s), vous etes : {categoryAge(age)}')

    i += 1

print('\n----------------------------------\n')


name = input('Entrez votre nom : ')
firstName = input('Entrez votre prénom : ')
age = getAgeUser()

print(f'{name} {firstName}, à {age} ans, vous etes \'{categoryAge(age)}\'.')