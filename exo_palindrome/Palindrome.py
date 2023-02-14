class Palindrome: 
    def __init__(self, phrase):
        self.phrase = phrase

    def estPalindrome(self):  
        palindrome = False

        for i in range(len(self.phrase)//2):
            if self.phrase[i] != self.phrase[-i-1]:
                palindrome = True
                break

        return palindrome