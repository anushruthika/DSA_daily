# 103. Binary Tree Zigzag Level Order Traversal

# Time: O(n) => all nodes traversed once
# Space: O(n) => queue + output storage

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        queue = deque([root])
        sign = 1
        
        while queue:
            level_size = len(queue)
            l = deque()
            
            for _ in range(level_size):
                cur = queue.popleft() # O(1)
                
                if sign == -1:
                    l.appendleft(cur.val)   # O(1)
                else:
                    l.append(cur.val)       # O(1)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            res.append(list(l))  # convert deque → list
            sign *= -1
        
        return res

## APPROACH 2: without using DEQUE
# Time: O(n²) => pop(0) + insert(0) cause shifting
# Space: O(n) => queue + output storage
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root:
            queue=[root]
            sign=1
            while queue:
                l=[]
                for i in range(len(queue)):
                    cur=queue.pop(0)
                    if sign == -1:
                        l.insert(0,cur.val)
                    elif sign==1:
                        l.append(cur.val) 
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                res.append(l)
                sign*=-1
        return res
                


                
        
