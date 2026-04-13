# 701. Insert into a Binary Search Tree

# Time: O(h) => traverse one path using BST property (worst O(n), best O(log n))
# Space: O(h) => recursive call stack (worst O(n), best O(log n))

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root

#iteration
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur = root
        prev = None
        while cur:
            if cur.val < val:
                prev = cur
                cur = cur.right
            else:
                prev = cur
                cur = cur.left
                
        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root
