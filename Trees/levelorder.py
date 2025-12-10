# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def levelorderrec(self,root,level,res):
        if root:
            if level>=len(res):
                res.append([])
            res[level].append(root.val)
            self.levelorderrec(root.left,level+1,res)
            self.levelorderrec(root.right,level+1,res)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levelorderrec(root,0,self.res)
        # c_res=[]
        # for i in self.res:
        #     for j in i:
        #         c_res.append(j)
        return self.res
