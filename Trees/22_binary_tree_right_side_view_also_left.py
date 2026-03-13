# 199. Binary Tree Right Side View


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root,res,level):
        if root:
            if level>=len(res):
                res.append([])
            res[level].append(root.val)
            self.bfs(root.left,res,level+1)
            self.bfs(root.right,res,level+1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.bfs(root,res,0)
        l=[]
        for i in res:
            # for left view
            # l.append(i[0])
            l.append(i[-1])
        return l
