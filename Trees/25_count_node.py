# 222. Count Complete Tree Nodes

# TC: O(log**2n)
# At each recursive level, I calculate the left and right heights in O(log n). 
# The recursion goes at most O(log n) levels because the tree is complete. Therefore the total time complexity is O(log² n).
# Space: O(logn)​
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def left_count(cur):
            count = 0
            while cur:
                cur = cur.left
                count+=1
            return count
        def right_count(cur):
            count = 0
            while cur:
                cur = cur.right
                count+=1
            return count
        lh = left_count(root)
        rh = right_count(root)
        if lh == rh:
            return 2**lh -1
        return 1+ self.countNodes(root.left)+ self.countNodes(root.right)
                    

                    

            

# Time: O(n) => all nodes traversed once
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ino(self,root,count):
        if root:
            self.ino(root.left,count)
            count[0]+=1
            self.ino(root.right,count)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=[0]
        self.ino(root,count)
        return count[0]


# 0ms code sample: 

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l,r,h = root,root,0
        while l and r: l,r,h = l.left,r.right,h+1
        return 2**h-1 if l==r else sum(map(self.countNodes,(root.left,root.right)))+1
