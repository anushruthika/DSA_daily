# https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1


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
        
