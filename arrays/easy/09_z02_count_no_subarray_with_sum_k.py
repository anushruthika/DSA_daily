# 560. Subarray Sum Equals K
# time: O(n)
# space: O(n) = > dict d
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        s = 0
        count = 0
        d = {}
        for i in range(len(nums)):
            s+=nums[i]
            if s == k:
                count = count+1
            rem = s-k
            if rem in d:
                count+=d[rem]
            if s not in d:
                d[s] = 1
            else:
                d[s]+=1
        return count
