## geek for geeks: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
# Time: O(n log n) => DFS O(n) + sorting columns & each column elements
# Space: O(n) => dictionary + recursion stack O(h)

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def dfs(self, root, d:dict, cur):
        row, col = cur

        if root.left:
            new_row, new_col = row + 1, col - 1
            if new_col in d:
                d[new_col].append((new_row, root.left.data))
            else:
                d[new_col]=[(new_row, root.left.data)]
            self.dfs(root.left, d, (new_row, new_col))

        if root.right:
            new_row, new_col = row + 1, col + 1
            if new_col in d:
                d[new_col].append((new_row, root.right.data))
            else:
                d[new_col]=[(new_row, root.right.data)]
            self.dfs(root.right, d, (new_row, new_col))
    def topView(self, root):
        res=[]
        if root:
            d = {0:[(0,root.data)]} 
            cur=(0,0)
            self.dfs(root,d,cur)
            for i in sorted(d.keys()):
                # Python sorts tuples lexicographically: (row1, val1) < (row2, val2) 
                # sort by row
                # if row equal → sort by value in the case of vertical order
                # column = sorted(d[i])  # sort by row then value
                
                # in the case of view only sort by row and column. dont sort by value
                column = sorted(d[i], key=lambda x: x[0]) # doesnot sort by value
                
                res.append(column[0][1])
        return res
        # code here
        
        
