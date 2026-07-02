# 34. Find First and Last Position of Element in Sorted Array
# TC: O(log n)
# SC: O(1)
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
    def upperBound(self, nums, target):
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]<=target:
                low = mid+1
            else:
                high=mid -1
        return low
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums,target)
        ub = self.upperBound(nums,target)
        if lb>=len(nums) or nums[lb]!=target:
            return [-1,-1]
        return [lb,ub-1]
