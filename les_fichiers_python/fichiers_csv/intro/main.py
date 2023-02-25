import os
import csv

file_path = os.getcwd() # récupérer le chemin absolu du répertoire de travail courant
file_path += "/les_fichiers_python/fichiers_csv/intro/employes_birthday.csv" # Obtenir le chemin du fichier

### Va lire le fichier csv et afficher en console chaque ligne :
with open(file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)


# DOC DICTREADER :
# Crée un objet qui opère comme un lecteur ordinaire mais assemble les informations de chaque ligne dans un dict dont les clés sont données par le paramètre optionnel fieldnames.
# Le paramètre fieldnames est une séquence. Si fieldnames est omis, les valeurs de la première ligne du fichier f sont utilisées comme noms de champs. Sans se soucier de comment sont déterminés les noms de champs, le dictionnaire préserve leur ordre original.
with open(file_path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')