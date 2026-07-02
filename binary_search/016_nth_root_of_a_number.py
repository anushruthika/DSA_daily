# https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

### OPTIMAL BINARY SEARCH similar to sqrt.
# TC:O(logn) SC:O(1)
class Solution:
    def nthRoot(self, n, x):
       # code here
        if x ==0 or x ==1:
            return x
        low = 1
        high = x
        while low<=high:
            mid = low+(high-low)//2
            val = mid**n
            if val == x:
                return mid
            elif val<x:
                low = mid+1
            elif val>x:
                high = mid-1
        return -1
