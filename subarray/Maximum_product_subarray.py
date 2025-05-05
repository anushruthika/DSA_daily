
import math
class Solution(object):
    def maxProduct(self, nums):
        min_pre=max_pre=max_prod=nums[0]
        for i in range(1,len(nums)):
            temp=max_pre
            max_pre = max(max_pre*nums[i],min_pre*nums[i],nums[i])
            min_pre = min(temp*nums[i],min_pre*nums[i],nums[i])
            if (max_prod < max_pre):
                max_prod=max_pre
        return max_prod
