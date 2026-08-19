class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        output, current = 0, 0
        l = 0

        for i in range(len(nums)):
            print(i)
            if nums[i] > threshold:
                current = 0

            elif current == 0:
                if nums[i] % 2 == 0:
                    current = 1

            elif nums[i] % 2 != nums[i - 1] % 2:
                current += 1

            else:
                if nums[i] % 2 == 0:
                    current = 1
                else:
                    current = 0

            output = max(output, current)

        return output