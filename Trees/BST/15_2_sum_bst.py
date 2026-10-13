
# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

Let n be the number of nodes and h be the tree height.

- **Time Complexity:** O(n) in the worst case. Each node is pushed and popped at most once per iterator.
- **Auxiliary Space:** O(h) for the two stacks.
- **Balanced BST:** h = O(log n), so auxiliary space is O(log n).
- **Skewed BST:** h = O(n), so auxiliary space is O(n).
class Solution:
    class BST:
        def __init__(self,root,reverse=False):
            self.stack = []
            self.reverse = reverse
            self.root = root
            self.push(self.root)
        def push(self,node):
            while node:
                if self.reverse:
                    self.stack.append(node)
                    node = node.right
                else:
                    self.stack.append(node)
                    node = node.left
        def next(self):
            if self.stack:
                cur = self.stack.pop()
                if self.reverse:
                    self.push(cur.left)
                else:
                    self.push(cur.right)
                return cur.val
            return -1
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        left = self.BST(root)
        right = self.BST(root,True)
        l = left.next()
        r = right.next()
        print(l,r)
        while l<r:
            if l+r == k:
                return True
            elif l+r<k:
                l= left.next()
            else:
                r= right.next()
        return False
        

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
