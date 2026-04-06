# 99. Recover Binary Search Tree

# Time: O(n) => inorder traversal visits each node once
# Space: O(h) => recursion stack (worst O(n), best O(log n))

class Solution:
    def inorder(self,node):
            if not node:
                return
            self.inorder(node.left)

            # Sorted Order Validation
            # first => from the node voilation beings
            # second => node violation ends
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node    
            self.prev = node
            
            self.inorder(node.right)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = None
        
        self.inorder(root)
        self.first.val,self.second.val = self.second.val ,self.first.val


        
        
