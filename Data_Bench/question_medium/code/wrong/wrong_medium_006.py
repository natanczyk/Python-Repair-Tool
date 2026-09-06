
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result="\u017DZZZZZZZZZZZZZZZ"
    
        def isLeaf(node):
            if(node):
               return ((not node.left) and (not node.right))
            return False
        
        def traversar(path,node):
            if (not node): return
            
            path+=chr(ord('a')+node.val)
            
            if(isLeaf(node) and path[::-1]<self.result):
            self.result=path[::-1]
            return
            
            traversar(path,node.left)
            traversar(path,node.right)

        traversar("",root)

        return self.result
