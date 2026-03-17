# https://www.naukri.com/code360/problems/childrensumproperty_790723
# eg: 3 7 5 50 1 2 30
#         50                            
#        /  \
#       7    2        => 
#      / \  / \
#     3  5 1  30

#         50
#        /  \
#      55    31        =>
#      / \   / \
#     50  5  1  30

#       86
#      /  \
#    55    31
#   /  \   / \
# 50   5  1  30

from os import *
from sys import *
from collections import *
from math import *

'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''  
def changeTree(root): 
    if not root:
        return

    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data

    if child < root.data:
        if root.left:
            root.left.data = root.data
        elif root.right:
            root.right.data = root.data

    changeTree(root.left)
    changeTree(root.right)

    tot = 0
    if root.left:
        tot += root.left.data
    if root.right:
        tot += root.right.data

    if root.left or root.right:
        root.data = tot
    pass
