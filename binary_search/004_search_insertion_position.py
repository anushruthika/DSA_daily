# 35. Search Insert Position
# TC:O(n) SC:O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if nums[0] == target or nums[0]>target:
            return 0
        for i in range(1,n):
            if nums[i] == target or nums[i-1] < target < nums[i]:
                return i
        return n

#############
# 35. Search Insert Position
# TC:O(logn) SC:O(1)
# x>= target
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+ (high-low)//2
            if nums[mid]<target:
                low = mid+1
            else: 
                high = mid-1
        return low
