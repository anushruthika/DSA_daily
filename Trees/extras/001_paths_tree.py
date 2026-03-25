# 257. Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,res,res1):
        if root:
            res.append(root.val)
            if root.left == None and root.right == None:
                res1.append(res.copy())
            self.dfs(root.left,res,res1)
            self.dfs(root.right,res,res1)
            res.pop()
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        res1=[]
        self.dfs(root,res,res1)
        res=[]
        return['->'.join(map(str,i)) for i in res1]
