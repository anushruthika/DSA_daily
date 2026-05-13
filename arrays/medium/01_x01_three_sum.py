# time O(n**2), space O(n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        k = 0
        res=set()
        for i,v in enumerate(nums[:-2]):
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-k-v-x]=1
                else:
                    res.add((x,v,k-v-x))
        return list(map(list,res))
