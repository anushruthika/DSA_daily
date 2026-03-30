# geeksforgeeks.org/problems/implementing-ceil-in-bst/1

# Time: O(h) => traverse one path using BST property (worst O(n), best O(log n))
# Space: O(1) => iterative, no extra space used

''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        if not root:
            return -1
        
        cur = root
        f = -1
        while cur:
            if cur.data>=x:
                f = cur.data
                cur = cur.left
            else:
                cur = cur.right
        return f
