################################################################################################################
########################################## Exercice Supp #######################################################
################################################################################################################
#   Ecrire une fonction qui prend en entrée une liste de tuples avec plusieurs informations sur des employés   #
#   d'une société(nom, prénom, age, adresse, ville de résidence, pays, salaire, nom de la société),            #
#   une liste de villes et un dictionnaire de taux de change entre les différentes devises.                    #
#                                                                                                              #
#   Deux fonctions doivent etre réalisées:                                                                     #
#       1. Une fonctions qui doit renvoyer un dictionnaire avec les noms de villes en tant que clé             #
#          et la somme des salaires en devise locale pour chaque ville en tant que valeur.                     #
#                                                                                                              #
#       2. Une fonction qui doit renvoyer un dictionnaire avec les noms des sociétés en tant que clés          #
#          et une liste contenant le nombre d'employés par société et la liste des pays (de ces employés)      #
#          => employes = { nom_societe : [ nbr_employe, [pays] ] }                                             #
################################################################################################################

# 1.
def salaire_par_ville(liste_employes, liste_villes, dict_taux_change):        
        salaire_ville = {}
       
        # Ajout des villes en clés du dictionnaire avec comme valeur : 0
        for ville in liste_villes:     
            salaire_ville[ville] = 0
        
        # Ajout du salaire total des employés par ville
        for employe in liste_employes:
            if employe[4] in salaire_ville.keys():         # Si la ville de l'employe est une clé du dico
                salaire_ville[employe[4]] += employe[6]    # Ajout du salaire à la clé 'ville'

        # Convertion salaire avec la devise
        for ville in salaire_ville.keys():
            if ville == 'Lyon':
                taux = dict_taux_change['EU']
            elif ville == 'London':
                taux = dict_taux_change['GBP']
            elif ville in ['New York', 'Seoul']:
                taux = dict_taux_change['USD']
            elif ville == 'Shanghai':
                taux = dict_taux_change['CNY']
    
            salaire_ville[ville] *= taux
        
        return salaire_ville

# 2.
def employes_par_societe(liste_employes):
    employes_societes = {}

    # Ajout des societés en clés du dictionnaire avec comme valeur: une liste vide contenant
    # le nombre d'employés égale à 0 et une liste de pays vide
    for employe in liste_employes:
        societe = employe[7]
        employes_societes[societe] = [0, []]

    # Ajout d'employés dans chaque société + nom du pays
    for employe in liste_employes:
        societe = employe[7]
        pays = employe[5]
        if pays not in employes_societes[societe][1]:       # Si le pays n'est pas encore présent dans la liste:
            employes_societes[societe][0] += 1              #       Ajouter une personne dans la société
            employes_societes[societe][1].append(pays)      #       Ajouter le pays de la société
        else:                                               # Sinon :
            employes_societes[societe][0] += 1              #       Ajouter une personne dans la société

    return employes_societes


def main():
    employes = [
        ("Dupont", "Jacques", 32, "5 rue des Lilas", "Lyon", "France", 5_000, "Google"),
        ("Grognont", "Eric", 31, "14 rue des Lilas", "Lyon", "France", 1_000, "Google"),
        ("Smith", "John", 25, "1 Main St", "New York", "USA", 7_000, "Microsoft"),
        ("Swanh", "Boss", 70, "100 Main St", "New York", "USA", 70_000, "Apple"),
        ("Brown", "Jane", 29, "10 Downing St", "London", "UK", 6_000, "Amazon"), 
        ("Wang", "Li", 27, "20 Peking Rd", "Shanghai", "China", 8_000, "Alibaba"),
        ("zi", "Lou", 27, "20 Peking Rd", "Shanghai", "China", 8_000, "Alibaba"),
        ("Ziou", "Loulou", 30, "28 Peking Rd", "Shanghai", "France", 500, "Alibaba"),
        ("Rigou", "Kim", 33, "30 Jeju St", "Seoul", "South Korea", 7_500, "Samsung"),
        ("Chang", "kimy", 33, "01 Jeju St", "Seoul", "South Korea", 10_000, "Apple")
        ]

    villes = ['Lyon', 'New York', 'London', 'Shanghai', 'Seoul']

    taux_change = {'EU' : 1, 'USD' : 0.98, 'GBP' : 1.13, 'CNY' : 0.14}

    print('Salaire total des employés en fonction de la ville :')
    print(salaire_par_ville(employes, villes, taux_change))

    print('\nDictionnaire { Société - [ nombre d\'employés [provenance des employés] ] } :')
    print(employes_par_societe(employes))


if __name__ == "__main__":
    main()