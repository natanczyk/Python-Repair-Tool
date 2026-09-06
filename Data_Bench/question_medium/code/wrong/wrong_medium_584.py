
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left[0], default=0), n - min(right[0], default=n))
