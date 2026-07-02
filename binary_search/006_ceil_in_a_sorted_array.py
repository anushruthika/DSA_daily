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
