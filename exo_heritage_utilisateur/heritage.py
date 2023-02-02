# Listes de projets || 'pr_' -> projet privé, non accessible au junior
projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def afficher_projets(self):
        for projet in projets:
            print(projet)

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"


#Classe fille de Utilisateur
class Junior(Utilisateur):
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

paul = Junior("Paul", "Durand")
arthur = Utilisateur("Jean", "Marleau")

print(arthur)
print(paul)

print('---------------')

print('Projets accessible à paul :')
paul.afficher_projets()
print('Projets accessible à arthur :')
arthur.afficher_projets()
