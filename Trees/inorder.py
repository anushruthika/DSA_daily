# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def inorder_rec(self,root,res):
        if root !=None:
            self.inorder_rec(root.left,res)
            res.append(root.val)
            self.inorder_rec(root.right,res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_rec(root,self.res)
        return self.res
        
        
