# 94. Binary Tree Inorder Traversal

class Solution:
    def __init__(self):
        self.res=[]   

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack=[]
        while cur != None or len(stack)>0:
            while cur !=None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.res.append(cur.val)
            cur = cur.right
        return self.res
