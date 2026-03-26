# 111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def root_2_leaf_path(self,root,path,res):
        if root:
            res.append(root.val)
            if not root.left and not root.right:
                path.append(res.copy())
            self.root_2_leaf_path(root.left,path,res)
            self.root_2_leaf_path(root.right,path,res)
            res.pop()
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            len_l = []
            path =[]
            res=[]
            self.root_2_leaf_path(root,path,res)
            for i in path:
                len_l.append(len(i))
            return min(len_l)
        return 0
