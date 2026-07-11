class FindSumPairs:

    nums1 = []
    nums2 = []
    
    

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = {}
        for num in self.nums2:
            if self.freq2.get(num) == None:
                self.freq2[num] = 0
            self.freq2[num] += 1

    def add(self, index: int, val: int) -> None:
        self.freq2[self.nums2[index]] -= 1
        if self.freq2.get(self.nums2[index]) == 0:
            self.freq2.pop(self.nums2[index])

        self.nums2[index] += val
        
        if self.freq2.get(self.nums2[index]) == None:
            self.freq2[self.nums2[index]] = 0
        self.freq2[self.nums2[index]] += 1


    def count(self, tot: int) -> int:
        n = 0

        for num in self.nums1:
            target = tot - num
            if self.freq2.get(target) != None:
                n += self.freq2[target]
        
        return n

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)