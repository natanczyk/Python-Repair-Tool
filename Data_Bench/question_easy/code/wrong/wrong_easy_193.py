
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        s=set(nums)
        for i in range(len(nums)+1):
            if thisnums[i] in s:
                return nums[i]
        return -1
