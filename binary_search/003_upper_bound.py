# https://www.geeksforgeeks.org/problems/implement-upper-bound/1
# TC:O(logn) SC:O(n)
# X > target (if arr[mid]==target: then low=mid-1)
class Solution:
    def upperBound(self, arr, target):
        # code here
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+ (high-low)//2
            if arr[mid]>target:
                high = mid-1
            else: 
                low = mid+1
        return low
