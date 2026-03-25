# 515. Find Largest Value in Each Tree Row
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def bfs(root,res,level):
    #     if root:
    #         if level>=len(res):
    #             res.append([])
    #         res[level].append(root.val)
    #         self.bfs(root.left,res,level)
    #         self.bfs(root.right,res,level)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root:
            queue = [root]
            while queue:
                max_=float('-inf')
                for i in range(len(queue)):
                    node = queue.pop(0)
                    max_ = max(max_,node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(max_)
        return res
