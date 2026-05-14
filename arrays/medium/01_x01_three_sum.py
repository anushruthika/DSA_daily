# two pointer
# Time Complexity: O(n²)
# Space Complexity: O(n)

class Solution:
    def threeSum(self, nums):
        k =0
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n-2):
            l = i+1
            r = n-1
            while l<r:
                tot = nums[i]+nums[l]+nums[r]
                if tot < k:
                    l+=1
                elif tot > k:
                    r-=1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1  
                    r-=1
        return list(res)

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
