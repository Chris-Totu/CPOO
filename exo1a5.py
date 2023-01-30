import random

## Ex 1 ##
# Programme qui demande à l'utilisateur un nombre et qui dit à l'utilisateur si le nombre est pair ou impair
#
def isPeer():
    nbr = int(input('Entrez un nombre : '))
    if(nbr % 2 == 0):
        print(f'Le nombre {nbr} est pair.')
    else:
        print(f'Le nombre {nbr} est impair.')
        

## Ex 2 ##
# Programme qui demande à l'utilisateur deux nombres, fait la somme et divise par 2
def addDivision():
    nbr1 = int(input('Entrez premier nombre : '))
    nbr2 = int(input('Entrez second nombre : '))

    total = nbr1 + nbr2
    if(total == 0):
        print('Impossible de diviser 0 par 2')
    else:
        print(f'({nbr1} + {nbr2}) /2 = {total/2}')


## Ex 3 ##
# Programme qui prend un mot en entrée et qui va renvoyer le nombre de lettres de ce mot
def nbrLettresWord(word):
    nbrLettres = len(word)
    
    return nbrLettres


## Ex 4 ##
# Programme qui va aléatoirement tirer un nombre et qui va demander à l'utilisateur de deviner ce nombre.
# L'utilisateur a 10 tentatives pour trouver.
def findNbr():
    nbrAttempts = 1
    randNbr = random.randint(9, 99)
    userNbr = int(input('Entrez nombre : '))

    while nbrAttempts < 10 and userNbr != randNbr:
        nbrAttempts += 1
        userNbr = int(input(f'Retentez : '))
        
    if(randNbr == userNbr):
        print(f'Féliciation, vous avez trouvé le bon nombre en {nbrAttempts} !')
    else:
        print(f'Raté, le nombre à trouver était {randNbr}')


## Ex 5 ##
# Programme qui va aléatoirement tirer un nombre et qui va demander à l'utilisateur de deviner ce nombre + dire si c'est plus ou moins.
def findNbrMoreLess():
    nbrAttempts = 1
    randNbr = random.randint(9, 99)
    userNbr = int(input('Entrez nombre : '))

    while nbrAttempts < 10 and userNbr != randNbr:
        nbrAttempts += 1
        if(userNbr > randNbr):
            print('Nombre invalide, c\'est moins.')
        else:
            print('Nombre invalide, c\'est plus.')

        userNbr = int(input(f'Retentez : '))
        
    if(randNbr == userNbr):
        print(f'Féliciation, vous avez trouvé le bon nombre en {nbrAttempts} essai(s)!')
    else:
        print(f'Raté, le nombre à trouver était {randNbr}')


def main():
    print("Exo1:\n---")
    isPeer()
    
    print("Exo2:\n---")
    addDivision()
    
    print("Exo3:\n---")
    word = 'cancrelat.'
    nbrLetters = nbrLettresWord(word)
    print(f"Dans '{word}' il y'a {nbrLetters} lettre(s)")

    print("Exo4:\n---")
    findNbr()

    print("Exo5:\n---")
    findNbrMoreLess()


if __name__ == "__main__":
    main()