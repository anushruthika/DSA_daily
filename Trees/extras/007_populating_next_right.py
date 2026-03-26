"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 116. Populating Next Right Pointers in Each Node

class Solution:
    def dfs(self,root):
        if root:
            flag =0
            if root.left:
                if root.right:
                    flag = 1
                    root.left.next = root.right
                elif root.next:
                    if root.next.left:
                        flag = 1
                        root.left.next = root.next.left
                    elif root.next.right:
                        flag = 1
                        root.left.next = root.next.right
                if flag == 0:
                    root.left.next = None
            self.dfs(root.left)
            flag =0 
            if root.right:
                if root.next:
                    if root.next.right:
                        flag = 1
                        root.right.next = root.next.left
                    elif root.next.right:
                        flag =1
                        root.right.next = root.next.right
                if flag ==0:
                    root.right.next = None

            self.dfs(root.right)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            root.next=None
            self.dfs(root)
        return root
        
