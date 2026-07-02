# 81. Search in Rotated Sorted Array II
# TC: O(log n)
# SC: O(1)
class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+(high-low)//2
            if arr[mid] == target:
                return True

            ############ DUPLICATES condition
            if arr[mid] == arr[high] and arr[high] == arr[low]:
                low += 1
                high -= 1
                continue
            #################################
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
        return False
