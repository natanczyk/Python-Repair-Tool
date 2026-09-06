
class Solution:
    def makeSubKSumEqual(self, A: List[int], K: int) -> int:
        lA = len(A)
        g = gcd(lA, K)
        retV = 0
        for i in range(g):
            med = int(median(A[i:g]))
            retV += sum(abs(a-med) for a in A[i:g])
            
        return retV
