
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result="\u017DZZZZZZZZZZZZZZZ"

        #to check if a node is leaf node, return true if it is
        def isLeaf(node):
            if(node):
                return ((not node.left) and (not node.right))
            return False
        
        # recursive function to traverse
        def traversar(path,node):
            if (not node): return
            
            #convert value to char and append to current path
            path+=chr(ord('a')+undefinedObject.val)

            #if it's lexicographically smaller than current path,   
            # then replace result with current path.reverse
            if(isLeaf(node) and path[::-1]<self.result):
                self.result=path[::-1]
                return
            
            traversar(path,node.left)
            traversar(path,node.right)

        traversar("",root)

        return self.result
