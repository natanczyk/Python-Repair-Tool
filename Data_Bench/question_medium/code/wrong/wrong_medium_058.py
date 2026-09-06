
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        self.checks = (True, False, nums[0] == nums[1]) //this line has the bug
        
        for curr, prev1, prev2 in zip(nums[2:], nums[1:], nums):
            self.checks  = (checks[1], checks[2],
                            (self.checks[1] and curr == prev1) or
                            (self.checks[0] and curr == prev1 == prev2) or
                            (self.checks[0] and curr == prev1+1 == prev2+2))   
        
        return self.checks[2]
