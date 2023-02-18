from pathlib import Path
import pdb #Python débeuger
import os


def main():
    current = os.getcwd() # récupérer le chemin absolu du répertoire de travail courant
    chemin_fichier = Path("./test.txt").resolve() # Obtenir le chemin du fichier
    print(chemin_fichier)
    print(current)
    #Le programme va s'arreter à cette ligne avec 'pdb.set_trace'
    #pdb.set_trace()
    
    ## Ouverture du fichier en mode lecture ##
    #mon_doc = open(chemin_fichier, "r") # -> ne fonctionne pas, aucune idée pq
    mon_doc = open(f'{current}/les_fichiers_python/test.txt', 'r')
    
    # Lecture du fichier
    fichier = mon_doc.read()
    print(fichier)
    mon_doc.close()
    
    ## Ouverture du fichier en mode écriture ##
    mon_doc = open(f'{current}/les_fichiers_python/test.txt', 'a')
    # Ecriture dans le fichier
    mon_doc.write("\nJe vous dit que c'est un fichier, moi !")
    mon_doc.close()

    ## Ouverture du fichier en mode lecture ##
    mon_doc = open(f'{current}/les_fichiers_python/test.txt', 'r')
    # Lecture du fichier
    fichier = mon_doc.read()
    print(fichier)
    mon_doc.close()
    

if __name__ == "__main__":
    main()