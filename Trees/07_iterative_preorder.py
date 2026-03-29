# 144. Binary Tree Preorder Traversal

# Time: O(n), Space: O(n) (output) + O(h) stack (worst O(n), best O(log n))

class Solution:
    def __init__(self):
        self.res=[]
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = [root]
        while stack:
            cur = stack.pop()
            self.res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return self.res
