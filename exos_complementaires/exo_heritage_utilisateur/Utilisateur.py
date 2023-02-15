from projets import projets

class Senior:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def afficher_projets(self):
        for projet in projets:
            print(projet)

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

        
#Classe fille de Utilisateur
class Junior(Senior):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

    #Surcharge, on modifie la méthode:
    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith('pr_'):
                print(projet)

    #Polymorphisme, on augmente la méthode:
    def __str__(self):
        return super().__str__() + ' (Junior)'