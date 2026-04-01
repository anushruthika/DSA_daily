# Time: O(h) => search + possible successor traversal (worst O(n), best O(log n))
# Space: O(h) => recursive call stack (worst O(n), best O(log n))

# 450. Delete Node in a BST

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val == key:
                if not root.right:
                    return root.left
                if not root.left:
                    return root.right
                if root.right and root.left:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    root.val= temp.val
                    root.right = self.deleteNode(root.right,root.val)
            elif root.val > key:
                root.left = self.deleteNode(root.left,key)
            else:
                root.right = self.deleteNode(root.right,key)
            return root
