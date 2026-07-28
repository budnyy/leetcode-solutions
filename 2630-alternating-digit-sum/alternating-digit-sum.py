class Solution:
    def alternateDigitSum(self, n: int) -> int:
        output = 0
        positive = True
        nArray = list(map(int, str(n)))
        for num in nArray:
            if positive:
                output += num
                positive = False
            else:
                output -= num
                positive = True
        return output