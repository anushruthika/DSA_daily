# 103. Binary Tree Zigzag Level Order Traversal

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
                


                
        
