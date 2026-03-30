# 700. Search in a Binary Search Tree

# Time: O(h) => follow one path using BST property (worst O(n), best O(log n))
# Space: O(1) => iterative, no extra space used
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:            
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return -1
        cur = root
        while cur:
            print(cur.val)
            if cur.val==val:
                return cur
            if cur.val<val:
                cur = cur.right
            else:
                cur = cur.left
        return None



### BRUTE FORCE



# Time: O(n) => may traverse all nodes
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree)

class Solution:
    def node(self,root,val,res):
        if root!=None:
            if root.val == val:
                res[0] = root
            self.node(root.left,val,res)
            self.node(root.right,val,res) 
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = [None]
        self.node(root,val,node)
        return node[0]
