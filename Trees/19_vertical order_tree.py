# 987. Vertical Order Traversal of a Binary Tree
# Time: O(n log n) => DFS O(n) + sorting columns & each column elements
# Space: O(n) => dictionary + recursion stack O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        d = defaultdict(list) # d[col] = (row,val)
        def dfs(node,r,c):
            if node:
                d[c].append((r,node.val))
                if node.left:
                    dfs(node.left,r+1,c-1)
                if node.right:
                    dfs(node.right,r+1,c+1)
        dfs(root,0,0)
        res = []
        for col in sorted(d.keys()):
            res.append([i[1] for i in sorted(d[col])])
        return res





class Solution:

    def dfs(self, root, d:dict, cur):
        row, col = cur

        if root.left:
            new_row, new_col = row + 1, col - 1
            if new_col in d:
                d[new_col].append((new_row, root.left.val))
            else:
                d[new_col]=[(new_row, root.left.val)]
            self.dfs(root.left, d, (new_row, new_col))

        if root.right:
            new_row, new_col = row + 1, col + 1
            if new_col in d:
                d[new_col].append((new_row, root.right.val))
            else:
                d[new_col]=[(new_row, root.right.val)]
            self.dfs(root.right, d, (new_row, new_col))

    def verticalTraversal(self, root):
        res=[]
        if root:
            d = {0:[(0,root.val)]} 
            cur=(0,0)
            self.dfs(root,d,cur)
            for i in sorted(d.keys()):
                # Python sorts tuples lexicographically: (row1, val1) < (row2, val2) 
                # sort by row
                # if row equal → sort by value
                column = sorted(d[i])  # sort by row then value
                
                res.append([val for row, val in column])
        return res

        

            
            
                

        
