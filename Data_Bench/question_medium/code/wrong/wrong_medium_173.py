
class Solution:
    def minimumPartition(self, s: str, k: int) -> int
        
        for d in s:
            if int(d) > k:
                return -1
            curr = 10 * curt + int(d)
            if curr > k:
                ans += 1
                curr = int(d)
        return ans
