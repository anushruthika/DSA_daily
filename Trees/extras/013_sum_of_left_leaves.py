# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,res):
        if not root:
            return
        self.dfs(root.left,res)
        if root.left and not root.left.left and not root.left.right:
            res.append(root.left.val)
        self.dfs(root.right,res)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = []
        self.dfs(root,res)
        return sum(res)
