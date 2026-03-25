# 113
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        res1=[]
        self.dfs(root,res,targetSum,res1)
        return res1

    def dfs(self,root,res,sum_,res1):
        if root:
            res.append(root.val)
            if root.left == None and root.right == None and sum(res)==sum_:
                res1.append(res.copy())
            self.dfs(root.left,res,sum_,res1)
            self.dfs(root.right,res,sum_,res1)
            res.pop()
