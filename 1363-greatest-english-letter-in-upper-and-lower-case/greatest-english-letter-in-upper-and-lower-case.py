class Solution(object):
    def greatestLetter(self, s):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        available = []
        greatest = ""

        for letter in alphabet:
            if letter in s and letter.lower() in s:
                available.append(letter)

        if len(available) > 0:
            greatest = max(available)
        
        return greatest