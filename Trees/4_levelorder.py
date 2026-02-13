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

# TEST CODE
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data=val
        self.left = left
        self.right=right
def levelorder(root,res,level):
    if root:
        if level>=len(res):
            res.append([])
        res[level].append(root.data)
        levelorder(root.left,res,level+1,)
        levelorder(root.right,res,level+1)
    
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
levelorder(root, res,0)

for node in res:
    print(node, end=" ")
    
        
    
