# 1161. Maximum Level Sum of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root:
            queue = [root]
            max_=float('-inf')
            count=0
            while queue:
                res=[]
                count+=1
                for i in range(len(queue)):
                    node = queue.pop(0)
                    res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if sum(res)>max_:
                    max_=sum(res)
                    level=count
                
            return level
