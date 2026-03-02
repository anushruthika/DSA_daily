# 144. Binary Tree Preorder Traversal
class Solution:
    def __init__(self):
        self.res=[]
    # def preorder_rec(self,root,res):
    #     if root:
    #         res.append(root.val)
    #     if root and root.left !=None:
    #         self.preorder_rec(root.left,res)
    #     if root and root.right !=None:
    #         self.preorder_rec(root.right,res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = [root]
        while stack:
            cur = stack.pop()
            self.res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return self.res
