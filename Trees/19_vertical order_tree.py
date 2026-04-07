# 987. Vertical Order Traversal of a Binary Tree
# Time: O(n log n) => DFS O(n) + sorting columns & each column elements
# Space: O(n) => dictionary + recursion stack O(h)

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

        

            
            
                

        
