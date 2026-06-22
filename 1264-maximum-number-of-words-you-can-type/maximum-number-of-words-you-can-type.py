class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        
        words = text.split()

        for word in words:
            impos_word = False
        
            for bLetter in brokenLetters:
                if bLetter in word:
                    impos_word = True
                
            if not impos_word:
                count += 1 
           
        return count