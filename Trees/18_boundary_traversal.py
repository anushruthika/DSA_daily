# https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

# Points to remember:
# append root first
# go towards left tree dont append leaf
# iterate left tree & right tree seperately to find leaves
# go towards right tree dont append leaf




class Solution:
    def isleaf(self,root,res):
        if root:
            if not root.left and not root.right:
                res.append(root.data)
                return
            self.isleaf(root.left,res)
            self.isleaf(root.right,res)
    def boundaryTraversal(self, root):
        if not root:
            return []
        res=[root.data]
        if root.left:
            cur = root.left
            while cur:
                if cur.left or cur.right:
                    res.append(cur.data)
                if cur.left:
                    cur = cur.left
                # elif not cur.right:
                #     break
                else:
                    cur=cur.right
        self.isleaf(root.left,res)
        self.isleaf(root.right,res)
        stack=[]
        if root.right:
            stack=[]
            cur=root.right
            while cur:
                if cur.left or cur.right:
                    stack.append(cur)
                if cur.right:
                    cur = cur.right
                # elif not cur.right:
                #     break
                else:
                    cur=cur.left
            while stack:
                res.append(stack.pop().data)
        return res
                    
            
        
                    
            
                
                
