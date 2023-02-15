class Palindrome: 
    def __init__(self, phrase):
        self.phrase = phrase

    def estPalindrome(self):  
        # Convertit la phrase en minuscules et supprime les espaces
        phrase = self.phrase.lower() 
        # Vérifie si la phrase est égale à elle-même inversée et imprime True ou False
        return phrase == phrase[::-1]