
# 230. Kth Smallest Element in a BST

# Time: O(h + k) => traverse left path + process k nodes (worst O(n), best O(log n + k))
# Space: O(h) => stack stores path from root to leaf (worst O(n), best O(log n))
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        stack = []
        cur = root
        count = 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                count+=1
                cur = stack.pop()
                if count == k:
                    return cur.val
                cur = cur.right

# Time: O(n) => full inorder traversal of all nodes
# Space: O(n) => storing inorder list + recursion stack (worst O(n), best O(log n) for stack)
class Solution:
    def rec(self, root,res):
        if root:
            self.rec(root.left,res)
            res.append(root.val)
            self.rec(root.right,res)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.rec(root,res)
        return res[k-1]
