class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxValue = 0
        index = 0
        for m in range(len(mat)):
            sumN = 0
            sumN = sum(mat[m])
            if sumN > maxValue:
                index =  m
            maxValue=max(maxValue,sumN)
        return [index,maxValue]