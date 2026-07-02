# https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1
# TC: O(log n)
# SC: O(1)
# upper bound , if upper bound not found low must have traversed end thus return -1
class Solution:
    def findCeil(self, arr, x):
        # code here
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+ (high-low)//2
            if arr[mid]<x:
                low = mid+1
            else:
                high = mid-1
        if low>=len(arr):
            return -1
        return low
