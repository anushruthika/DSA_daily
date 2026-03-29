# 94. Binary Tree Inorder Traversal

# Time: O(n) => Each node is visited exactly once, 
# Space: O(n) (output=self.res,Stores all n nodes ) + O(h) recursion stack (worst(skewed tree) O(n), best(balanced tree) O(log n))

# recursion stack=> Recursion uses stack memory. All calls stay in memory until the deepest call returns.

# eg: skewed Tree
# 1
#  \
#   2
#    \
#     3
#      \
#       4

# recursion stack: stores all these to return back to the root
# call(1)
#   → call(2)
#     → call(3)
#       → call(4)

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
root.right.right = Node(6)

res = []
inorder(root, res)

for node in res:
    print(node, end=" ")
        
        
