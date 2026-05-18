# 559. Maximum Depth of N-ary Tree

class Solution:
    def dfs(self,root,res,count):
        if not root:
            return
        res[0] = max(res[0],count)
        for child in root.children:
            self.dfs(child,res,count+1)  
        # print(count)
    def maxDepth(self, root: 'Node') -> int:
        res = [0]
        self.dfs(root,res,1)
        return res[0]
