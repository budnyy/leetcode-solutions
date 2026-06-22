class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        
        words = text.split()

        for word in words:
            impos_word = False

            for letter in word:
            
                for bLetter in brokenLetters:
                    if letter == bLetter:
                        impos_word = True
                
            if impos_word:
                count -= 1 

            count += 1
        return count