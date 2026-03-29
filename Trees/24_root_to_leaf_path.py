# https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

# Time: O(n * h) => each path copy takes O(h), done for nodes
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree) + O(n*h) output

from typing import Optional
from collections import deque

from typing import List

class Solution:
    def ino(self, root, res, res2):
        if root:
            res.append(root.data)
            if not root.left and not root.right:
                # when ever the backtracking takes place: 
                # lists are mutable so the data will be delete
                res2.append(res.copy())
            else:
                self.ino(root.left,res,res2)
                self.ino(root.right,res,res2)
            res.pop()

    def Paths(self, root):
        res2 = []
        res = []
        self.ino(root, res, res2)
        return res2


#129. Sum Root to Leaf Numbers
class Solution:
    def rec1(self,root,s,res):
        if root:
            s+=str(root.val)
            if not root.left and not root.right :
                res.append(s)
            else:
                self.rec1(root.left,s,res)
                self.rec1(root.right,s,res)
            s=s[:-2]
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s=''
        r=[]
        self.rec1(root,s,r)
        return sum(list(map(int,r)))
