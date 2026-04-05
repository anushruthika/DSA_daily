# Time: O(1) amortized per next() / hasNext() => each node is pushed and popped at most once (total O(n) over all operations)
# Space: O(h) => stack stores path from root to current node (worst O(n), best O(log n))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack =list()
        self.push(root)

    def next(self) -> int:
        if self.stack:
            cur = self.stack.pop()
            self.push(cur.right)
            return cur.val
    def push(self,cur):
        while cur:
            self.stack.append(cur)
            cur = cur.left
    def hasNext(self) -> bool:
        return True if self.stack else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
