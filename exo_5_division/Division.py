class Division:
    tab_result = []
    
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        if(denominateur == 0):
            raise ZeroDivisionError("Le dénominateur ne peut pas être égal à 0")
        else:
            self.denominateur = denominateur
        self.tab_result.append(round(self.numerateur / self.denominateur, 2)) # à chaque création d'objet, le résultat est ajouté dans la liste "tab_result"

    # Affichage de la fraction en console
    def affichage_fraction(self):
        print(f" {self.numerateur}\n----\n {self.denominateur}")
    
    # Calcul de la division
    def result_division(self):
        return round(self.numerateur / self.denominateur, 2)
    
    # Affichage de tout les calculs qu'il y'a eu en console
    @staticmethod
    def all_results():
        print(Division.tab_result)