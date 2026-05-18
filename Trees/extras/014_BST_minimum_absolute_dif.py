# 530. Minimum Absolute Difference in BST

class Solution:

    def inorder_rec(self, root, m, prev):

        if root:

            self.inorder_rec(root.left, m, prev)

            if prev[0] is not None:

                m[0] = min(m[0], root.val - prev[0])

            prev[0] = root.val

            self.inorder_rec(root.right, m, prev)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        m = [float('inf')]

        prev = [None]

        self.inorder_rec(root, m, prev)

        return m[0]
