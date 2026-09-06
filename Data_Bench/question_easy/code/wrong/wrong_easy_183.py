
class Solution:
    def findTheArrayConcVal(self, nums) -> int:
        i=0
        c=0
        j=len(nums)-1
        while(i<=j):
            if(i==j):
                c=c+num[i]
                break
            s=str(nums[i])+str(nums[j])
            c=c+int(s)
            i=i+1
            j=j-1
        return c
