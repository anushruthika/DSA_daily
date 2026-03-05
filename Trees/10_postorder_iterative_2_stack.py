# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = []
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            stack1=[root]
            stack2=[]
            while stack1:
                cur=stack1.pop()
                stack2.append(cur)
                if cur.left:
                    stack1.append(cur.left)
                if cur.right:
                    stack1.append(cur.right)
            while stack2:
                self.res.append(stack2.pop().val)
                
        return self.res
