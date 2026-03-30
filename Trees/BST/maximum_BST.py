# no where to solve

# Time: O(h) => traverse leftmost/rightmost path (worst O(n), best O(log n))
# Space: O(1) => no extra space used

class Solution:
    def findMax(self,root):
        while root.right!=None:
            root= root.right
        return root.data
    def findMin(self,root):
        while root.left!=None:
            root= root.left
        return root.data
