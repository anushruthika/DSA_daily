# 1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ino(self, root, s, res2):
        if root:
            s+=str(root.val)
            if not root.left and not root.right:
                res2.append(s)
            else:
                self.ino(root.left,s,res2)
                self.ino(root.right,s,res2)
            s= ''   
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res2 = []
        s=''
        self.ino(root, s, res2)
        return sum(map(lambda x: int(x, 2), res2))
