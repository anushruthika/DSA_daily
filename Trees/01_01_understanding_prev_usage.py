# 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,prev):
        if root:
            if prev[0] and prev[0]!=root.val:
                return False
            prev[0] = root.val
            return self.dfs(root.left,prev) and self.dfs(root.right,prev)
        if not root:
            return True

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root,[None])
