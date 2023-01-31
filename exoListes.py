## Programme qui échange les valeurs du premier avec le dernier élément de la liste.
def swap_list(list):
    lenList = len(list) - 1
    list[0], list[lenList] = list[lenList], list[0]
    return list


## Écrire un programme qui prend en entrée un chiffre et qui vérifie si ce chiffre appartient à la liste suivante : [43,-34,67,89,790].
## Si oui, on félicite l’utilisateur et on quitte le programme. Sinon, on l’invite à recommencer.
def check_number(n):
    numbers = [43, -34, 67, 89, 790]
    isPresent = False
    while not isPresent:
        if n in numbers:
            print("Félicitations, votre nombre est dans la liste !")
            isPresent = True
        else:
            print("Désolé, votre nombre n'est pas dans la liste, veuillez recommencer.")        
            n = int(input("Entrez un nombre : "))


# Sur base de l’énoncé précédent, pouvez-vous optimiser la recherche ? Si oui, comment ?
# -> heeeu oui sans doute avec une boucle for.


## 'Optimiser' ce programme en suggérant à l’utilisateur si il s’est trompé si son chiffre doit être plus grand ou plus petit
# pour se retrouver dans la liste.
def check_number_v2(n):
    numbers = sorted([43, -34, 67, 89, 790])
    minNbr, maxNbr = numbers[0], numbers[-1]
    isPresent = False
    
    while not isPresent:
        if n in numbers:
            print("Félicitations, votre nombre est dans la liste !")
            isPresent = True
        else:
            if n < minNbr:
                print("Désolé, votre nombre est trop petit, veuillez recommencer.")        
                n = int(input("Entrez un nombre : "))
            elif n > maxNbr:
                print("Désolé, votre nombre est trop grand, veuillez recommencer.")        
                n = int(input("Entrez un nombre : "))
            else:
                print("Désolé, votre nombre est ni trop grand, ni trop petit, mais incorrect, veuillez recommencer.")        
                n = int(input("Entrez un nombre : "))


def last_exercise():
    ## Soit la liste suivante :
    L = [ 987, 65, 43, 21, 43, 98, 145 ]
    # • Afficher la liste L
    print(L)
    
    # • Compter le nombre d'occurrences de 43 dans L
    print(L.count(43))

    # • Ajouter le nombre 45 en dernière position, afficher L
    L.append(45)
    print(L)

    # • Afficher la longueur de la liste
    print(len(L))

    # • Supprimer un élément 43 de L, afficher L
    L.remove(43)
    print(L)

    # • Refaire 2.
    print(L.count(43))

    # • Renverser l'ordre de L ; afficher L
    L.reverse()
    print(L)
    
    # • Trier L, afficher L
    L.sort()
    print(L)

    # • Supprimer le dernier élément, afficher L
    L.pop()
    print(L)



def main():
    animals = ['chat', 'chien', 'rat', 'elephant']
    print(swap_list(animals))

    check_number(3)

    check_number_v2(45)

    last_exercise()


if __name__ == "__main__":
    main()