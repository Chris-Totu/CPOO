# Ecrivez une classe Voiture 
# Elle disposera de méthodes permettant:
    # • Augmenter la vitesse en lui passant la vitesse en argument
    # • Diminuer la vitesse en lui passant la vitesse en argument
    # • Obtenir la vitesse actuelle
class Voiture:
    def __init__(self, vitesse, marque):
        self.marque = marque
        self.vitesse = vitesse

    def augmentation_vitesse(self, vitesse):
        self.vitesse += vitesse

    def diminution_vitesse(self, vitesse):
        if(self.vitesse - vitesse < 0):
            self.vitesse = 0
        else:
            self.vitesse -= vitesse
    
    def obtention_vitesse(self):
        return self.vitesse


    def __str__(self):
        return f'La voiture de marque {self.marque} roule à une vitesse de {self.vitesse}km/h.'