# TC: O(log n)
# SC: O(1)
# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+(high-low)//2
            if arr[mid] == target:
                return mid
            # left sorted array
            if arr[low]<=arr[mid]:
                if arr[low]<=target and arr[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            # right sorted array
            else:
                if arr[high]>=target and arr[mid]<target:
                    low = mid+1
                else:
                    high = mid-1
        return -1
        
