class Solution:
    def pivotInteger(self, n: int) -> int:
        start = 0
        finish = n
        j, i = 1, 1

        if n == 1:
            return 1

        while i < n:
            start += i
            i += 1
            
            if finish < start:
                finish += (n - j)
                j += 1
            
            if i == (n - j) and start == finish:
                return i

        return -1
