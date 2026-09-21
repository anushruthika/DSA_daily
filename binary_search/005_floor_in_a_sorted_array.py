# TC: O(log n)
# SC: O(1)
# same upper bound but return high

# floor == Upper bound -1 (floor == ans is element before strictly greater than x therefore up-1)
#  upper bound -1: example: 
[11,11,25]     x: 12 upbound : 25 floor: upbound-1: 11
[11,11,25]     x: 11 upbound: 25 (strictly greater) upbound-1: 11

# Ceil == lower bound (greater or equal == definition of lb)
[9,11,11,25] x:12 lb: 25 ceil: 25 
[9,11,11,25] x:11 lb: 11 ceil: 11
class Solution:
    def findFloor(self, arr, x):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1

        return high
