# 18. 4Sum

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        k = target
        res = set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                l = j+1
                r = n-1
                while l<r:
                    tot = nums[i]+nums[j]+nums[l]+nums[r]
                    if tot==k:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
                    elif tot<k:
                        l+=1
                    else:
                        r-=1
        return list(res)
