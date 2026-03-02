# 104. Maximum Depth of Binary Tree
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,root,level,res):
        if root:
            if level>=len(res):
                res.append([])
            res[level].append(root.val)
            self.rec(root.left,level+1,res)
            self.rec(root.right,level+1,res)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=[]
        self.rec(root,0,res)
        return len(res)

        
