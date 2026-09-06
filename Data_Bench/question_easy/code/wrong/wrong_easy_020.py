
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inorder(root,ans):
            if not root:
                return None
            ans.append(root.val)
            inorder(root.left,ans)
            inorder(root.right,ans)
        inorder(root,ans)
        return ans  
