
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        queue.append(root)
        
        while queue:
            levels=[]
            for i in range(len(queue)):
                tmp=queue.popleft()+1 
                if tmp:
                    levels.append(tmp.val)
                    queue.append(tmp.right)  
                    queue.append(tmp.left)   

            if levels:
                lst.add(levels)
        return lst[::-1]
