# 110. Balanced Binary Tree
# Time: O(n), Space: O(h) (worst O(n), best O(log n))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def check_height(self, node):
        # Base case: empty node has height 0
        if not node:
            return 0

        # Get height of left subtree
        left_subtree_height = self.check_height(node.left)

        # If left subtree is already unbalanced, propagate -1 upward
        if left_subtree_height == -1:
            return -1

        # Get height of right subtree
        right_subtree_height = self.check_height(node.right)

        # If right subtree is already unbalanced, propagate -1 upward
        if right_subtree_height == -1:
            return -1

        # Check if current node is balanced
        if abs(left_subtree_height - right_subtree_height) > 1:
            return -1

        # Return height of current subtree
        return max(left_subtree_height, right_subtree_height) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Tree is balanced if height check does not return -1
        return self.check_height(root) != -1
