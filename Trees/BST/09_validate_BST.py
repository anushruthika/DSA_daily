# 98. Validate Binary Search Tree

# Time: O(n) => visit each node once
# Space: O(h) => recursion stack (worst O(n), best O(log n))

class Solution:
    def validate(self, root,low,high):
        if root:
            if not (low<root.val<high):
                return False
            return self.validate(root.left,low,root.val) and self.validate(root.right,root.val,high)
        return True  
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float('-inf'), float('inf'))

# Time: O(n log n) => inorder traversal O(n) + sorting O(n log n) + set check O(n)
# Space: O(n) => storing inorder list + set + recursion stack (worst O(n), best O(log n) for stack)
class Solution:
    def rec(self, root,res):
        if root:
            self.rec(root.left,res)
            res.append(root.val)
            self.rec(root.right,res)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.rec(root,res)
        if res == sorted(res) and len(set(res)) == len(res):
            return True
        else:
            return False
