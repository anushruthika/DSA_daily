# 94. Binary Tree Inorder Traversal

# Time: O(n) => Each node is visited exactly once, 
# Space: O(n) (output=self.res,Stores all n nodes ) + O(h) stack (worst(skewed tree) O(n), best(balanced tree) O(log n))

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
