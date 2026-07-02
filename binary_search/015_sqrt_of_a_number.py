# 69. Sqrt(x)

### BUILT IN:
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(x**(0.5))
### BRUTE force linear search

########OPTIMAL BINARY SEARCH
# TC: o(logn) SC:O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x ==1:
            return x
        low = 1
        high = x
        while low<=high:
            mid = low+(high-low)//2
            val = mid*mid
            if val == x:
                return mid
            elif val<x:
                low = mid+1
            elif val>x:
                high = mid-1
        return high
        
