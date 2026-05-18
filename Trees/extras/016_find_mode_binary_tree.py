# 501. Find Mode in Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,window,prev,mw,val):
        if root:
            self.dfs(root.left,window,prev,mw,val)
            if prev[0]!=None:
                if prev[0]==root.val:
                    window[0]+=1
                else:
                    window[0]=1
            if window[0]>mw[0]:
                mw[0]=window[0]
                val.clear()
                val.append(root.val)
            elif window[0] == mw[0]:
                val.append(root.val)
            prev[0] = root.val
            self.dfs(root.right,window,prev,mw,val)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mw = [float('-inf')]
        val=[]
        self.dfs(root,[1],[None],mw,val)
        return val
