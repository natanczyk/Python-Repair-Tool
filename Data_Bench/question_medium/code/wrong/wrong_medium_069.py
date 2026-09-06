
class Solution:

        lst,val,tmp=[],[],[]
        for i in nums:
            if i==pivot:val.append(i)
            elif i<pivot:lst.append(i)
            else:tmp.append(i)
        return lst+val+tmp
