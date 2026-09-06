
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(numbers) <= 2:
            return -1
        else:
            return sorted(numbers)[-2]
