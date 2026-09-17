# https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

### OPTIMAL BINARY SEARCH similar to sqrt.
# TC:O(logn) SC:O(1)
# TC:O(log(n/2)) SC:O(1)
class Solution:
    def nthRoot(self, n, m):
        if m == 0 or m ==1 or n ==1:
            return m
       # code here
        low = 1
        high = m//2+1
        while low<=high:
            mid = low+(high-low)//2
            root = mid**n
            if root == m:
                return mid
            elif root>m:
                high = mid-1
            else:
                low = mid+1
        return -1
            
