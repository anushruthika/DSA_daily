# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum_rec(self,root,d):
        if not root:
            return 0
        s_l=self.sum_rec(root.left,d)
        s_r=self.sum_rec(root.right,d)
        l=max(0,s_l)
        r=max(0,s_r)
        d[0] = max(d[0],root.val+l+r)
        return root.val+max(l,r)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        d=[float('-inf')]
        self.sum_rec(root,d)
        return d[0]
