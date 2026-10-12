# https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
class Solution:
    def findUnion(self, a, b):
        i = 0
        j = 0
        n = len(a)
        m = len(b)
        c = []
        while i<n and j<m:
            if a[i]<=b[j]:
                if not c or (c and c[-1]!=a[i]):
                    c.append(a[i])
                i+=1
            elif b[j]<a[i]:
                if not c  or ( c and c[-1]!=b[j]):
                    c.append(b[j])
                j+=1
        while i<n:
            if not c or (c and c[-1]!=a[i]):
                c.append(a[i])
            i+=1
        while j<m:
            if not c  or ( c and c[-1]!=b[j]):
                c.append(b[j])
            j+=1
        return c
