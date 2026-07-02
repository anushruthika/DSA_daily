# TC: O(log n)
# SC: O(1)
# same lower bound but return high
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
