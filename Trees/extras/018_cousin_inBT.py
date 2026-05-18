# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def level(self,root,parent,level,x,y,info):
        if root:
            if parent: 
                if root.val == x:
                    info[0] = (parent,level)
                if root.val == y:
                    info[1] = (parent,level)
            self.level(root.left,root,level+1,x,y,info)
            self.level(root.right,root,level+1,x,y,info)
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        info = {}
        self.level(root,None,0,x,y,info)
        if len(info)==2:
            return (info[0][0]!= info[1][0] and info[1][1] == info[0][1])
        return False
