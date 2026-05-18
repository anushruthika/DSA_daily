# 897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,res):
        if root:
            self.dfs(root.left,res)
            res.append(root.val)
            self.dfs(root.right,res)
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        self.dfs(root,res)
        res_root = TreeNode(res[0])
        cur = res_root
        for i in range(1,len(res)):
            cur.right = TreeNode(res[i])
            cur.left = None
            cur = cur.right
        return res_root
