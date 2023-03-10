from math import pi

class Forme():
    def perimeter(self):
        print("Perimeter is not defined for this shape.")


class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote
    
    def perimeter(self):
        return self.cote * 4


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimeter(self):
        return (self.longueur + self.largeur) * 2
    
    
class Cercle(Forme):
    def __init__(self, diameter):
        self.diameter = diameter

    def perimeter(self):
        return self.diameter * pi
    