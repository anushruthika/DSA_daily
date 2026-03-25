# 1448
class Solution:
    def dfs(self,root,res,count):
        if root:
            if res and root.val >= max(res):
                count[0]+=1
            res.append(root.val)
            self.dfs(root.left,res,count)
            self.dfs(root.right,res,count)
            res.pop()
    def goodNodes(self, root: TreeNode) -> int:
        count=[1]
        res=[]
        self.dfs(root,res,count)
        return count[0]
