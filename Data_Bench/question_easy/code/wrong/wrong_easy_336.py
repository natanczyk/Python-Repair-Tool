
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        val = count.values()
        import math
        m = math.gcd(*val)
        if m >= 3:
            return True 
        else:
            return val[2]
