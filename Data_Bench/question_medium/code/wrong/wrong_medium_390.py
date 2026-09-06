
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lst,val,tmp=[],[],[]
        for i in nums:
            if i<pivot:val.append(i)
            elif i==pivot:lst.append(nums[i])
            else:tmp.append(nums[i])
        nums[]return lst+val+tmp
