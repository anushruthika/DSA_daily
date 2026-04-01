# 235. Lowest Common Ancestor of a Binary Search Tree
# Time: O(h) => traverse one path using BST property (worst O(n), best O(log n))
# Space: O(1) => iterative, no extra space used
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        large = max(p.val,q.val)
        small = min(p.val,q.val)
        while cur:
            if cur.val > large:
                cur = cur.left
            elif cur.val < small:
                cur = cur.right
            else:
                return cur
        return None
