
# 637. Average of Levels in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        if root:
            queue = [root]
            while queue:
                sum_=0
                n= len(queue)
                for i in range(n):
                    node = queue.pop(0)
                    sum_+=node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(sum_/n)
        return res
