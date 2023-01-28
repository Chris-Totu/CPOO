import random

nbrRows = 10
nbrColumns = 4
nbrColor = 4
colorsAvailable = ["BLEU", "JAUNE", "ROUGE", "NOIR"]

""" Initialise et return un master mind vierge """
def initMasterMind():
    return [['xxxxx' for i in range(nbrColumns)] for y in range(nbrRows)]

""" Initialise la table de coups erronés / justes vierge """
def initErrorsTable():
    return ['_ _ _ _ ' for i in range(nbrRows)]

""" Affiche le master mind et la table des coups """
def displayMasterMind(masterMind, errorsTable):
    position = 0
    line = nbrRows  
    print('\n          |       Master Mind         |  Tableau erreurs\n*******************************************************')
    for row in masterMind:
        print(f"Ligne {line}  {'|' if line > 9 else ' |'}  {' '.join(row)}  |     {errorsTable[position]}")
        position += 1
        line -= 1


"""Return une combinaison mystere de couleur"""
def getColorsMyst():
    colorMyst = ['']*4
    for i in range(nbrColor):
        random_num = random.randint(0, 3)
        colorMyst[i] = colorsAvailable[random_num]

    return colorMyst


"""Return le tableau de couleur de l'utilisateur."""
def getUserColors():
    





masterMind = initMasterMind()
errorTable = initErrorsTable()
displayMasterMind(masterMind, errorTable)
colormyst = getColorsMyst()
