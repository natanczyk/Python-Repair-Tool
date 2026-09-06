
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        if s1 == s2:
            return True
        for k in range(1, len(s1)+1):
            if (
                self.isScramble(s1[k:], s2[k:]) and self.isScramble(s1[:k], s2[:k])
            ) or (
                self.isScramble(s1[k:], s2[:-k]) and self.isScramble(s1[:k], s2[-k:])
            ): return True
        return False
