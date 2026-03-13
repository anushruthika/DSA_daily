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
    def bottomView(self, root):
        res=[]
        if root:
            d = {0:[(0,root.data)]} 
            cur=(0,0)
            self.dfs(root,d,cur)
            for col in sorted(d.keys()):

                max_row = float('-inf')
                val = None

                for r,v in d[col]:
                    if r >= max_row:   # >= keeps the last occurrence
                        max_row = r
                        val = v

                res.append(val)
        return res
        # code here
        
        
        
