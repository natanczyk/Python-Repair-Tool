
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        b = True
        for n in derived:
            b = not b if n else b
        return 
