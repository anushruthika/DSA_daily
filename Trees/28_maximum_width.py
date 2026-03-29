# 662. Maximum Width of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n) => all nodes processed once
# Space: O(n) => queue stores nodes level-wise

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            queue=[[root,1]]
            level=0
            res=[]
            while queue:
                res.append([])
                for i in range(len(queue)):
                    node = queue.pop(0)
                    res[level].append(node[1])
                    if node[0].left:
                        queue.append([node[0].left,(2*node[1])+0])
                    if node[0].right:
                        queue.append([node[0].right,(2*node[1])+1])
                level+=1
            max_p=float("-inf")
            for lev in res:
                max_p = max(max_p, max(lev) - min(lev) +1)
            return max_p
            

        
