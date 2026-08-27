# Time Complexity: O(N) Each node is process 3 times as (node,1),(node,2),(node,3) needs to be processed
# Space Complexity: O(N) to store preorder,inorder,postorder list
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # num = 1 -> pre order 2 -> in order 3-> post order
    stack = [[root,1]]
    preorder = []
    inorder = []
    postorder = []
    while stack:
        cur = stack[-1]
        if cur[1] == 1:
            stack[-1][1]+=1
            preorder.append(stack[-1][0].data)
            if cur[0].left:
                stack.append([cur[0].left,1])
        elif cur[1] == 2:
            stack[-1][1]+=1
            inorder.append(stack[-1][0].data)
            if cur[0].right:
                stack.append([cur[0].right,1])
        elif cur[1] == 3:
            stack.pop()
            postorder.append(cur[0].data)
    return inorder,preorder,postorder
