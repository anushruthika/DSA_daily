# 1. Two Sum
# time O(n)
# space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            if v in d:
                return [d[v],i]
            rem = target-v
            if rem not in d:
                d[rem] = i
