import random

class Chifoumi:
    def __init__(self):
        self.user_choice = ""
        self.ia_choice = ""
        self.possibilities = ['Pierre', 'Papier', 'Ciseau']
        self.victories = {'user' : 0, 'ia' : 0}
        self.most_used = {'Pierre' : 0, 'Papier' : 0, 'Ciseau' : 0}

    ### Méthodes
    def play(self):
        self.user_choice = input('Choix joueur : ')
        while self.user_choice not in self.possibilities:
            self.user_choice = input('Erreur encodement, réessayez : ')
        self.ia_choice = random.choice(self.possibilities)
        print("L'IA a choisi :", self.ia_choice)
        
        # ENCODER LES DATAS
        self.most_used[self.user_choice] += 1
        # ENCORE ENCODER LES DATAS MIAM LES DATAS
        self.most_used[self.ia_choice] += 1
        
        # Meme main :
        if self.user_choice == self.ia_choice:
            print("Match nul !")
        # Joeur >
        elif self.user_choice == 'Pierre' and self.ia_choice == 'Ciseau' or self.user_choice == 'Ciseau' and self.ia_choice == 'Papier' or self.user_choice == 'Papier' and self.ia_choice == 'Pierre':
            print("Joueur a gagné !")
            self.victories['user'] += 1
        # IA >
        else:
            print("L'IA a gagné !")
            self.victories['ia'] += 1

    def nbr_victories(self):
        # Savoir par utilisateur (CPU/Joueur), le nombre de victoires
        print("Nombre de victoire = Joeur : {} - IA : {}".format(self.victories['user'], self.victories['ia']))

    def nbr_used(self):
        # Savoir quel est le type le plus utilisé (ex: papier, pierre ou ciseau)
        max_choice = max(self.most_used.keys(), key = self.most_used.get)
        print(f"L'élément le plus utilisé est {max_choice} avec {self.most_used[max_choice]} utilisations.")

