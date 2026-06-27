# https://www.geeksforgeeks.org/problems/implement-lower-bound/1

# TC:O(logn) SC:O(1)
class Solution:
    def lowerBound(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            # 1. Corrected operator precedence
            mid = low + (high - low) // 2 
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1 
        return low 

