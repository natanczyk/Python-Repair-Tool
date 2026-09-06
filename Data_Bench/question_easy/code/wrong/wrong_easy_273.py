
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool
        d=Counter(arr)
        l=self.get_values(d)
        print(l)
        if len(l)==len(set(l)):
            return True
        else:
            return False
