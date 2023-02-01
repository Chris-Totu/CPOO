from datetime import datetime

# Ecrire un dictionnaire qui aura comme clé :
# • Nom, prénom, age
# • Et comme valeur:
# • Dupont, Davi, 30
person = {'name': 'Dupont',
          'firstName' : 'Davi',
          'age': 30}


# • Corriger l’erreur dans le prénom avec la bonne valeur ‘David’
person['firstName'] = 'David'


# • Afficher la liste des clés et des valeurs
print('Clés :')
for k in person.keys():
    print(k)


print('\nValeurs :')
for v in person.values():
    print(v)


# • Afficher la liste des paires clés/valeurs
print('\nClés - Valeurs :')
for k, v in person.items():
    print(f'{k} - {v}')


# • Ecrire la phrase suivante: David Dupont a 30 ans
print(f"{person['name']} {person['firstName']} a {person['age']} {'ans' if person['age'] >= 2 else 'an'}.")


# • Ajouter une clé Date de naissance et renseigner ’17/01/1991’
person['birthDate'] = '17/01/1991'
print(person)


# • Age: fonction calculée sur base de la date de naissance (datetime)
def age(person):
    birth_date = datetime.strptime(person['birthDate'], '%d/%m/%Y')
    today = datetime.now()
    age = today.year - birth_date.year 
    return age

print(age(person))


# Créez un dictionnaire avec les informations suivantes sur une personne : nom, prénom, âge, ville de résidence. Affichez le dictionnaire.
infos_person = { 'name': 'Chris', 
                'firstname': 'Hoho',
                'age': 24,
                'homeCity': 'Soumoy'}
print(infos_person)

# • Ajoutez une clé supplémentaire 'pays' au dictionnaire ci-dessus avec la valeur appropriée.
infos_person['country'] = 'Belgium'


# • Écrivez une boucle pour afficher toutes les clés et valeurs du dictionnaire.
for k, v in infos_person.items():
    print(f'{k} : {v}')


# • Écrivez une fonction qui prend en entrée une liste de noms et renvoie un dictionnaire avec les noms en tant que clés et
# leur longueur en tant que valeurs.
def name_length_dict(names_list):
    name_lengths = {}
    for name in names_list:
        name_lengths[name] = len(name)
    return name_lengths

names_list = ['Chris', 'Louis', 'Joel', 'MelhiMelhoZebi']
print(name_length_dict(names_list))


# • Écrivez une fonction qui prend en entrée un dictionnaire et renvoie une liste de toutes les valeurs du dictionnaire.
def dict_to_list_values(dictio):
    list_values = []
    for key in dictio:
        list_values.append(dictio[key])
    return list_values 

names_dict ={'Chris' : 78, 'Louis': 555, 'Joel': 89559, 'MelhiMelhoZebi': 'eofjvev'}
print(dict_to_list_values(names_dict))


# • Écrivez une fonction qui prend en entrée deux listes et renvoie un dictionnaire avec les éléments
# de la première liste en tant que clés et les éléments de la seconde liste en tant que valeurs.
# • Écrivez une fonction qui prend en entrée un dictionnaire et renvoie une liste des clés triées dans
# l'ordre croissant des valeurs.