# 100. Same Tree
# Time: O(n) => all nodes compared once
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


# Time: O(n) => all nodes traversed once
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,root1,root2):
        if not root1 and root2:
            return -1
        elif root1 and not root2:
            return -1
        elif root1 and root2:
            if root1.val !=root2.val:
                return -1
            l = self.rec(root1.left,root2.left)
            if l ==-1:
                return -1
            l = self.rec(root1.right,root2.right)
            if l ==-1:
                return -1

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if self.rec(p,q)==-1:
            return False
        else:
            return True
        
