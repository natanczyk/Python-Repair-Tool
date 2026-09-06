
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(self.uniqueCandyTypes(candyType)))

    def uniqueCandyTypes(self, candyList):
        self.processCandyList(candyList)
