# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self,p,q):
        if p is None and q is None :
            return True
        if p is None or q is None :
            return False
        return p.val==q.val and self.isMirror(p.left,q.right) and self.isMirror(p.right,q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
        

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs_left(self,root,res,level):
        if level>=len(res):
            res.append([])
        if root:
            res[level].append(root.val)
            self.bfs_left(root.left,res,level+1)
            self.bfs_left(root.right,res,level+1)
        else:
            res[level].append(None)
    def bfs_right(self,root,res,level):
        if level>=len(res):
            res.append([])
        if root:
            res[level].append(root.val)
            self.bfs_right(root.right,res,level+1)
            self.bfs_right(root.left,res,level+1)
        else:
            res[level].append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            res_left = []
            self.bfs_left(root.left,res_left,0)
            res_right = []
            self.bfs_right(root.right,res_right,0)
            if res_left == res_right:
                return True
            else:
                return False

        
