class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if nums[0] == target or nums[0]>target:
            return 0
        for i in range(1,n):
            if nums[i] == target or nums[i-1] < target < nums[i]:
                return i
        return n
