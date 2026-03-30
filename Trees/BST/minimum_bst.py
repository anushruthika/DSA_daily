# https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1

# Time: O(h) => traverse leftmost path (worst O(n), best O(log n))
# Space: O(1) => no extra space used

class Solution:
    def minValue(self, root):
        while root.left!=None:
            root= root.left
        return root.data
