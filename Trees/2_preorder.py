# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def preorder_rec(self,root,res):
        if root:
            res.append(root.val)
        if root and root.left !=None:
            self.preorder_rec(root.left,res)
        if root and root.right !=None:
            self.preorder_rec(root.right,res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder_rec(root,self.res)
        return self.res


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data=val
        self.left = left
        self.right=right
def preorder(root,res):
    if root == None:
        return
    res.append(root.data)
    preorder(root.left,res)
    preorder(root.right,res)

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
# Preorder:
# 1 2 4 5 3 6 7
# Inorder:
# 4 2 5 1 6 3 7
# Postorder:
# 4 5 2 6 7 3 1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res = []
preorder(root, res)

for node in res:
    print(node, end=" ")
    
        
    
        
