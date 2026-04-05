
# https://www.geeksforgeeks.org/problems/merge-two-bst-s/1

# Time: O(n + m) => inorder traversals O(n + m) + merging two sorted lists O(n + m)
# Space: O(n + m) => storing inorder lists + merged list + recursion stack (worst O(n + m), best O(log n + log m))
class Solution:
    def rec(self, root, res):
        if root:
            self.rec(root.left, res)
            res.append(root.data)
            self.rec(root.right, res)
    def merge_sort(self,res1,res2):
        i=0
        j=0
        ans=[]
        while i<len(res1) and j<len(res2):
            if res1[i]<res2[j]:
                ans.append(res1[i])
                i+=1
            else:
                ans.append(res2[j])
                j+=1
        if res1:
            ans.extend(res1[i:])
        if res2:
            ans.extend(res2[j:])
        return ans
    def merge(self, root1, root2):
        res1 =[]
        res2 =[]
        self.rec(root1,res1)
        self.rec(root2,res2)
        
        # return sorted(res1+res2)
        return self.merge_sort(res1,res2)


# Time: O((n + m) log(n + m)) => inorder traversals O(n + m) + sorting merged list
# Space: O(n + m) => storing both inorder lists + merged list + recursion stack (worst O(n + m), best O(log n + log m))

class Solution:
    def rec(self, root, res):
        if root:
            self.rec(root.left, res)
            res.append(root.data)
            self.rec(root.right, res)
    def merge(self, root1, root2):
        res1 =[]
        res2 =[]
        self.rec(root1,res1)
        self.rec(root2,res2)
        return sorted(res1+res2)
