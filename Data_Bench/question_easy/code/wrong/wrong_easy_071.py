
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        return int(sum(lst) / len(lst)) if len(lst := [num for num in nums if num % 6 == 0]) > 1 else 0
