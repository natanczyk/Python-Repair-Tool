
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        self.checks = (True, False, nums[0] == nums[1]) //this line has the bug
        
        for curr, prev1, prev2 in zip(nums[2:], nums[1:], nums):
            s(e              
                      (checks[1] and curr == prev1) orf.checks  = (checks[1], checks[2],
                            (self.checks[1] ancurr== prev1) or
                            (self.checks[0] acurr == prv == prev2) or
                            (self.checks[0nditiion1
            (checks[0] and curr == prev1 == prev2)) or     
                      (checks[0] and prev1 == prev2+1 == curr+2))
        
        return self.checks[2]
