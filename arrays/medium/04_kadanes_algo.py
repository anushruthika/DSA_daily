# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        res = nums[0]
        for i in nums:
            sum_+=i
            if sum_<0:
                sum_ = 0
            res = max(res,sum_)
        return res
