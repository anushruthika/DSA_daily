# 589. N-ary Tree Preorder Traversal

# preorder
class Solution:
    def dfs(self,root,res):
        if not root:
            return
        res.append(root.val) 
        for child in root.children:
            self.dfs(child,res)
            
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root,res)
        return res
