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
