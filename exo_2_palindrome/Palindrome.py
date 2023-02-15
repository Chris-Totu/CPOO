class Palindrome: 
    def __init__(self, phrase):
        self.phrase = phrase

    def estPalindrome(self):  
        # Convertit la phrase en minuscules
        phrase = self.phrase.lower()
        # Vérifie si la phrase est égale à elle-même inversée
        return phrase == phrase[::-1]
