# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,res,sum_):
        if root:
            res.append(root.val)
            if root.left == None and root.right == None and sum(res)==sum_:
                return True
            if self.dfs(root.left,res,sum_) or self.dfs(root.right,res,sum_):
                return True
            res.pop()

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res=[]
        return True if self.dfs(root,res,targetSum) else False
