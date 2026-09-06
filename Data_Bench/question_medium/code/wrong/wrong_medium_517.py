
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        max_memo, min_memo = nums[0], nums[0]
        for num in nums[1:]
            max_memo, min_memo = max(max_memo, num, num*max_memo, num*min_memo), min(min_memo, num, num*min_memo, num*max_memo)
        return max_memo
