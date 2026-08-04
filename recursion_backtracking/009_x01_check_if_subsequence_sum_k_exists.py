#  brute force:
class Solution:
    def __init__(self):
        self.res = []
    def rec(self,res_until_now,total,start,target,nums):
        if target<total:
            return
        if target == total:
            self.res.append(res_until_now[:])
            return
        for ind in range(start,len(nums)):
            res_until_now.append(nums[ind])
            self.rec(res_until_now,total+nums[ind],ind+1,target,nums)
            res_until_now.pop()
    def checkSubsequenceSum(self, arr, k):
        self.rec([],0,0,k,arr)
        return self.res !=[]

# OPtimal


class Solution:
    def rec(self, total, start, target, nums):
        if total == target:
            return True

        if total > target:
            return False

        for i in range(start, len(nums)):
            if self.rec(total + nums[i], i + 1, target, nums):
                return True

        return False

    def checkSubsequenceSum(self, arr, k):
        return self.rec(0, 0, k, arr)
