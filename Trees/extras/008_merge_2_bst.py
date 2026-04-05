# https://leetcode.com/problems/merge-two-binary-trees/

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 and root2:
            ans= TreeNode(root1.val+root2.val)
            ans.left = self.mergeTrees(root1.left,root2.left)
            ans.right = self.mergeTrees(root1.right,root2.right)
            return ans
        else:
            return root1 or root2
