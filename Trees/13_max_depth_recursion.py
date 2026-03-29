# 104.Maximum Depth of a binary Tree

# Time: O(n) => all nodes traversed once
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree)


class Solution:
    def rec(self,root):
        if not root:
            return 0
        left_height=self.rec(root.left)
        right_height=self.rec(root.right)
        return max(left_height,right_height)+1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.rec(root)

        
