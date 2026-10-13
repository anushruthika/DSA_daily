# 15. 3Sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        k = 0
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = n-1
            while l<r:
                tot = nums[i]+nums[l]+nums[r]
                if tot == k:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif tot<k:
                    l+=1
                else:
                    r-=1
                
        return list(res)
