class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbin = str(format(x, '032b'))
        ybin = str(format(y, '032b'))
        i = 0
        count = len(xbin)

        while i < len(xbin):
            if xbin[i] == ybin[i]:
                count -= 1
            i += 1
        return count

