# 563. Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,res):
        if not root:
            return 0
        if not root.right and not root.left:
            return root.val
        dl = self.dfs(root.left,res)
        dr = self.dfs(root.right,res)
        res.append(abs(dr-dl))
        return dl+dr+root.val
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = []
        self.dfs(root,res)
        print(res)
        return sum(res)
