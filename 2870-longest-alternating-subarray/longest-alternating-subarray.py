class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        i , j = 0, 0
        output = 1
        temp = 1
        needBig = True
        for j in range(len(nums)):
            temp = 1
            needBig = True
            for i in range(j, len(nums) - 1):
                if nums[i + 1] == nums[i] + 1 and needBig:
                    temp += 1
                    needBig = not needBig
                    if temp > output:
                        output = temp
                elif nums[i + 1] == nums[i] -1 and not needBig:
                    temp += 1
                    needBig = not needBig
                    if temp > output:
                        output = temp
                else:
                    temp = 1
                    needBig = True
                    if temp > output:
                        output = temp
                    continue

        if output == 1:
            return -1
        return output

            

  