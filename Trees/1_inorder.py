# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def inorder_rec(self,root,res):
        if root !=None:
            self.inorder_rec(root.left,res)
            res.append(root.val)
            self.inorder_rec(root.right,res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_rec(root,self.res)
        return self.res

#### TEST CODE
# Inorder : left - root - right
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data=val
        self.left = left
        self.right=right
def inorder(root,res):
    if root == None:
        return
    inorder(root.left,res)
    res.append(root.data)
    inorder(root.right,res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

res = []
inorder(root, res)

for node in res:
    print(node, end=" ")
        
        
