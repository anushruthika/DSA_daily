# 145. Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def postorder_rec(self,root,res):
        if root !=None:
            self.postorder_rec(root.left,res)
            self.postorder_rec(root.right,res)
            res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder_rec(root,self.res)
        return self.res
