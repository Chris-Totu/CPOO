## Programme qui échange les valeurs du premier avec le dernier élément de la liste.
def exchangeList(list):
    lenList = len(list) - 1
    list[0], list[lenList] = list[lenList], list[0]
    return list

## Écrire un programme qui prend en entrée un chiffre et qui vérifie si ce chiffre appartient à la liste suivante : [43,-34,67,89,790].
## Si oui, on félicite l’utilisateur et on quitte le programme. Sinon, on l’invite à recommencer.

def main():
    animals = ['chat', 'chien', 'rat', 'elephant']
    print(exchangeList(animals))

if __name__ == "__main__":
    main()