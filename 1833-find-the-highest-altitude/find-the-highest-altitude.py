class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = 0
        highest = 0
        for g in gain:
            n += g
            if n > highest:
                highest = n 
        return highest