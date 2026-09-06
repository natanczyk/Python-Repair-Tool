from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter(nums)
        index = 0

        for num, count in counter.items():
            nums[index] = num
            index += 1
            if count > 1:
                nums[index] = num
                index += 1

        return index