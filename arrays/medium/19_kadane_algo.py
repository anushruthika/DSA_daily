# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if nums:
            sum_= 0
            max_sum = float('-inf')
            n = len(nums)
            for i in range(n):
                if sum_+nums[i]<0:
                    sum_ = 0
                    max_sum = max(max_sum,nums[i])
                else:
                    sum_ +=nums[i]
                    max_sum = max(max_sum,sum_)
            return max_sum
            
