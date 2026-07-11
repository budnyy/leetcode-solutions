class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        arrLen = len(nums)
        scoreArr = []
        i, j = 0, 0
        count = 0

        while i < arrLen:
            j = i
            if nums[i] % 2 == 0:
                while j < arrLen:
                    if nums[j] % 2 == 1:
                        count += 1
                    j += 1
                scoreArr.append(count)
            
            elif nums[i] % 2 == 1:
                while j < arrLen:
                    if nums[j] % 2 == 0:
                        count += 1
                    j += 1
                scoreArr.append(count)
            
            count = 0
            i+=1
            
        return scoreArr