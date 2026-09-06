
class Solution:                                 
    def sortArray(self,nums:list[int]) -> list[int]:    

        ctr  = Counter(nums)                            

        return list(chain(*([i]*ctr[i]                  
                    for i in range(min(ctr),            
                    max(ctr)+1) if i in let)))          
