class Voiture:
    voitures_crees = 0

    def __init__(self, marque, vitesse, prix):
        Voiture.voitures_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    # Methodes de classe : return une instance de classé prédéfinie
    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)

    # Methodes statique
    @staticmethod
    def afficher_nombre_voitures():
        print(f"Il a eu création de {Voiture.voitures_crees} {'voitures' if Voiture.voitures_crees > 2 else 'voiture'}.")

    # toString()
    def __str__(self) -> str:
        return f'Voiture de marque {self.marque} avec vitesse max limtée à {self.vitesse}.'

if __name__ == "__main__":
    peugeot = Voiture('Peugeot', 190, 50000)
    lambo = Voiture.lamborghini()
    porsche = Voiture.porsche()
    
    print(peugeot)
    print(lambo)
    print(porsche)
    Voiture.afficher_nombre_voitures()