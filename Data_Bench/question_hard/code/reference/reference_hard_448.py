class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gc=0
        for i in numsDivide:
            gc=int(math.gcd(gc,i))
        nums.sort()
        for i in range(len(nums)):
            if gc%nums[i]==0:
                return i
        return -1