class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            attempt = nums[mid]

            if attempt == target:
                return mid
            elif attempt < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1