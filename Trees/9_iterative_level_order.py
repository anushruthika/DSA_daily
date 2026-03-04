# 102. Binary Tree Level Order Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue=[root]
            while queue:
                l=[]
                for i in range(0,len(queue)):
                    node = queue.pop(0)
                    l.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                self.res.append(l)
        return self.res
