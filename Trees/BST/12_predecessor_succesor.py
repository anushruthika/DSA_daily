# https://www.geeksforgeeks.org/problems/predecessor-and-successor/1

# Time: O(n) => full inorder traversal of all nodes
# Space: O(h) => recursion stack (worst O(n), best O(log n))
class Solution:
    def rec(self, root,key):
        if root:
            self.rec(root.left,key)
            if root.data < key:
                self.pre = root
            if root.data>key and self.suc is None:
                self.suc = root
            self.rec(root.right,key)
    def findPreSuc(self, root, key):
        self.pre = None
        self.suc = None
        self.rec(root,key)
        return [self.pre,self.suc]


# Time: O(n) => inorder traversal O(n) + linear scan O(n) = O(n)
# Space: O(n) => storing inorder list + recursion stack (worst O(n), best O(log n))
class Solution:
    def rec(self, root, res):
        if root:
            self.rec(root.left, res)
            res.append(root)
            self.rec(root.right, res)

    def findPreSuc(self, root, key):
        res = []
        self.rec(root, res)

        pre, suc = None, None

        for i in range(len(res)):
            if res[i].data < key:
                pre = res[i]
            elif res[i].data > key:
                suc = res[i]
                break

        return [pre, suc]
