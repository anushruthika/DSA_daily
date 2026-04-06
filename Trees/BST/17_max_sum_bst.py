# 1373. Maximum Sum BST in Binary Tree

# Time: O(n) => each node is visited once (postorder traversal)
# Space: O(h) => recursion stack (worst O(n), best O(log n))

class Solution:
    def validate(self,root):
        if not root:
            return (True,0,float('inf'),float('-inf'))
        l_bool, l_val, l_low,l_high = self.validate(root.left)
        r_bool,r_val, r_low,r_high = self.validate(root.right)
        if l_bool and r_bool and l_high < root.val < r_low:
            cur_sum =l_val+r_val+root.val 
            self.max_sum = max(cur_sum, self.max_sum)
            return (True,cur_sum,min(l_low,root.val),max(r_high,root.val))
        return (False,0,0,0)

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        self.validate(root)
        return self.max_sum
