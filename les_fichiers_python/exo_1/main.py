## Ecrire un programme permettant de lire les données stockées dans
## un fichier et les copier dans un autre fichier


import os

def main():
    current = os.getcwd()
    print(current)
    with open(f'{current}/CPOO/les_fichiers_python/exo_1/fichier_source.txt', 'r') as f:
        saving = f.read()

    with open(f'{current}/CPOO/les_fichiers_python/exo_1/fichier_terminus.txt', 'w') as f:
        f.write(saving)
    
if __name__ == "__main__":
    main()
