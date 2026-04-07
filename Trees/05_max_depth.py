# 104. Maximum Depth of Binary Tree

# Time: O(n) => all nodes traversed once
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree)
class Solution:
    def rec(self,root):
        if not root:
            return 0
        lh = self.rec(root.left)
        rh = self.rec(root.right)
        return max(lh,rh)+1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.rec(root)



# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Time: O(n) => Each node is visited exactly once, 
# Space: O(n) (output=self.res,Stores all n nodes ) + O(h) recursion stack (worst(skewed tree) O(n), best(balanced tree) O(log n))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,root,level,res):
        if root:
            if level>=len(res):
                res.append([])
            res[level].append(root.val)
            self.rec(root.left,level+1,res)
            self.rec(root.right,level+1,res)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=[]
        self.rec(root,0,res)
        return len(res)

### ITERATIVE APPROACH
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level_count=0
        if root: 
            queue = [root]
            while queue:
                for i in range(0,len(queue)):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level_count+=1
        return level_count
        
