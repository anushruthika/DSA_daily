# 104.Maximum Depth of a binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,root):
        if not root:
            return 0
        left_height=self.rec(root.left)
        right_height=self.rec(root.right)
        return max(left_height,right_height)+1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.rec(root)

        
