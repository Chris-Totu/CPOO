import json
import os

from constants import DATA_DIR

class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!")
        
        if element in self:
            print(f"{element} est déjà dans la liste.")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")

    def sauvergarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)

        return True

if __name__ == "__main__":
    liste = Liste("courses")  
     
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.enlever("Pommes")
    liste.ajouter("Oranges")
    liste.sauvergarder()