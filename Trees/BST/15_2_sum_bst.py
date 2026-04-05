
# 653. Two Sum IV - Input is a BST

# Time: O(n) => each node visited once + O(1) set lookup per node
# Space: O(n) => set stores up to n elements + recursion stack (worst O(n), best O(log n))
class Solution:
    def rec(self, root,seen,k):
        if root:
            if root.val in seen:
                return True
            seen.add(k-root.val)
            return self.rec(root.left,seen,k) or self.rec(root.right,seen,k) 
        return False
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        return self.rec(root,seen,k)
      
# iterations
# Time: O(n) => inorder traversal visiting each node once + O(1) set lookup per node
# Space: O(n) => set stores up to n elements + stack (worst O(n), best O(log n))

class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = []
        l = set()
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur.val in l:
                    return True
                else:
                    l.add(k-cur.val)
                cur = cur.right
        return False
