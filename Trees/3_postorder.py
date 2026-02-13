# 145. Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def postorder_rec(self,root,res):
        if root !=None:
            self.postorder_rec(root.left,res)
            self.postorder_rec(root.right,res)
            res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder_rec(root,self.res)
        return self.res


# TEST CODE
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data=val
        self.left = left
        self.right=right
def postorder(root,res):
    if root == None:
        return
    postorder(root.left,res)
    postorder(root.right,res)
    res.append(root.data)

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
postorder(root, res)

for node in res:
    print(node, end=" ")
    
        
    
