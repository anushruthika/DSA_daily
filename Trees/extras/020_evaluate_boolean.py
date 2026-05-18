# 2331. Evaluate Boolean Binary Tree

class Solution:
    def __init__(self):
        self.res=[]
    def inorder_rec(self,root):
        if not root.left and not root.right:
            return root.val
        l = self.inorder_rec(root.left)
        r = self.inorder_rec(root.right)
        if root.val  == 2:
            return l or r
        elif root.val == 3:
            return l and r
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return bool(self.inorder_rec(root))
