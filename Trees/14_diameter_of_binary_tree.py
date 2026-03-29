# 543. Diameter of Binary Tree

# Time: O(n) => all nodes traversed once
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_height(self,root,d):
        if not root:
            return 0
        left_height = self.check_height(root.left,d)
        right_height = self.check_height(root.right,d)
        d[0]=max(d[0],left_height+right_height)
        return max(left_height,right_height)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=[0]
        self.check_height(root,d)
        return d[0]
