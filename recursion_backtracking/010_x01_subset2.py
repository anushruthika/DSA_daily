# 90. Subsets II

# [] -> [[]]
class Solution:
    def __init__(self):
        self.res = []
    def rec(self,res_until_now,start,nums):
        self.res.append(res_until_now[:])
        for ind in range(start,len(nums)):
            if ind>start and nums[ind]==nums[ind-1]:
                continue
            self.rec(res_until_now+[nums[ind]],ind+1,nums)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<0:
            return [[]]
        nums.sort()
        self.rec([],0,nums)
        return self.res
