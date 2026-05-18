# 671. Second Minimum Node In a Binary Tree

class Solution:
    def dfs(self,root,m):
        if not root:
            return
        self.dfs(root.left,m)
        
        if root.val<m[0]:
            m[1] = m[0]
            m[0]=root.val
        elif m[1]>root.val>m[0]:
            m[1] = root.val
        # print(root.val,m,m[0],m[1])
        self.dfs(root.right,m)
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        m=[float('inf'),float('inf')]
        self.dfs(root,m)
        if m[1] == float('inf'):
            return -1
        return m[1]
