# 572. Subtree of Another Tree
# SIMILAR TO SYMMETRIC TREE
class Solution:
    def isSameTree(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        if self.isSameTree(root, subRoot): 
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
