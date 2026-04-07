# 114. Flatten Binary Tree to Linked List

# Time: O(n) => DFS O(n) + rebuilding O(n)
# Space: O(n) => O(h) recursion stack + O(n) list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def serialize(self,root):
        def dfs(root,res):
            if root:
                res.append(root.val)
                dfs(root.left,res)
                dfs(root.right,res)
        res=[]
        s=dfs(root,res)
        return res
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = self.serialize(root)
        if root:
            root.left = None
            cur = root
            for i in res:
                cur.right=TreeNode(i)
            


        
