# brute force TC: O(n**2) search (n)(n-1)(n-2...)
class Solution:
    def minWindow(self, s, t):
        n = len(s)
        m = len(t)
        i=0
        j=0
        k=0
        l = float('inf')
        res = ''
        while i<n and j<n:
            if s[j] == t[k]:
                k+=1
            if k == m:
                if l>j-i+1:
                    l = j-i+1  
                    res = s[i:j+1]
                i=i+1
                j=i
                k=0
                continue
            j+=1
        return res
