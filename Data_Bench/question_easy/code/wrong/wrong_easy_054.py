
class Solution:
    def thirdMax(self, nums) -> int:
        return self.max(list(set(nums))) if len(list(set(nums)))<3 else sorted(list(set(nums)))[-3]
