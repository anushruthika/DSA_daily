# geeksforgeeks.org/problems/floor-in-bst/1

# Time: O(h) => traverse one path using BST property (worst O(n), best O(log n))
# Space: O(1) => iterative, no extra space used

class Solution:
    def findFloor(self, root, x):
        if not root:
            return -1
        
        cur = root
        f = -1
        while cur:
            if cur.data<=x:
                f = cur.data
                cur = cur.right
            else:
                cur = cur.left
        return f
