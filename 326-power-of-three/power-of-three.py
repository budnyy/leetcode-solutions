#horrible code
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n >= 3:
            while n > 3:
                if n % 3 != 0:
                    return False
                n = n // 3
            if n % 3 != 0:
                    return False
            return True
        return False
            
                
            