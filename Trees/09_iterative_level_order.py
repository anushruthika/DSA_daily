# 102. Binary Tree Level Order Traversal

# Time : O(n) Each node is processed exactly once => popleft() is O(1)
# space: O(n)
# Explanation: Queue: can hold up to one full level → O(n)
# Output (self.res): stores all nodes → O(n) 
# O(n) + O(n) = O(2n) = O(n) => In Big-O, we drop constants 

from collections import deque


class Solution:
    def __init__(self):
        self.res=[]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            # queue=[root]
            queue = deque([root])
            while queue:
                l=[]
                for i in range(0,len(queue)):
                    node = queue.popleft() # popleft() is O(1)
                    l.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                self.res.append(l)
        return self.res

        
### APPROACH 2=> without using deque 
# Time : O(n^2) Each node is processed exactly once => pop(0) is O(n)
# space: O(n)
# Explanation: Queue: can hold up to one full level → O(n)
# Output (self.res): stores all nodes → O(n) 
# O(n) + O(n) = O(2n) = O(n) => In Big-O, we drop constants 

class Solution:
    def __init__(self):
        self.res=[]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue=[root]
            while queue:
                l=[]
                for i in range(0,len(queue)):
                    node = queue.pop(0) # popleft() is O(1) pop(0) is O(n)
                    l.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                self.res.append(l)
        return self.res
### APPROACH : LEVEL COUNT INT TRACKER INSTEAD OF L LIST TRACKER
class Solution:
    def __init__(self):
        self.res=[]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_count=0
        if root: 
            queue = [root]
            while queue:
                self.res.append([])
                for i in range(0,len(queue)):
                    node = queue.pop(0)
                    self.res[level_count].append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level_count+=1       
        return self.res
