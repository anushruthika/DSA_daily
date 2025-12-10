# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def preorder_rec(self,root,res):
        if root:
            res.append(root.val)
        if root and root.left !=None:
            self.preorder_rec(root.left,res)
        if root and root.right !=None:
            self.preorder_rec(root.right,res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder_rec(root,self.res)
        return self.res
        
