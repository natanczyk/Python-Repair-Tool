
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # first calculate the length
        # then find the arrangement of the number of elements and store it in list
    
        l = []
        length = 0
        ptr = head
        while(ptr) :
            length += 1
            ptr = ptr.next

        # possible length of the elements of an node to split
        # first find how much it will be posiibe to split by length // k
        # then calculate the remaining no of elements by length % k
        arrange = []
        maxi = len//k 
        remain = len%k

        for i in range(k) :
            if remain :
                arrange.push(maxi + 1)  
                remain -= 1
            else:
                arrange.push(maxi)

        # now traverse the linked list and split the node 
        j = 0
        ptr = head 
        i = 0
        while(ptr) :
            q = ptr 
            i += 1
            ptr = ptr.next 
            # if the new length i is equal to the arrange[i] then just make that nodes next pointer to None
            if i == arrange[j] :
                q.next = None
                l.push(head)
                head = ptr 
                i = 0
                j += 1

        # if the length is not satisfied then just add none
        for i in range(j,k+1):
            l.push(None)
        return l
