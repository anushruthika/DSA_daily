
# 590. N-ary Tree Postorder Traversal
class Solution:
    def dfs(self,root,res):
        if not root:
            return
        for child in root.children:
            self.dfs(child,res)
        res.append(root.val)   
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root,res)
        return res
