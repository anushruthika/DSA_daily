# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ino(self,root,count):
        if root:
            self.ino(root.left,count)
            count[0]+=1
            self.ino(root.right,count)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=[0]
        self.ino(root,count)
        return count[0]


# 0ms code sample: 

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l,r,h = root,root,0
        while l and r: l,r,h = l.left,r.right,h+1
        return 2**h-1 if l==r else sum(map(self.countNodes,(root.left,root.right)))+1
