
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return max(len(candyType)//2, len(set(candyType)))
