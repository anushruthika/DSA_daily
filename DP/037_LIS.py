# 300. Longest Increasing Subsequence
# O(n**2)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        DP = [[-1] * (n + 1) for _ in range(n)]

        def rec(ind, prevInd):
            if ind < 0:
                return 0

            if DP[ind][prevInd + 1] != -1:
                return DP[ind][prevInd + 1]

            not_take = rec(ind - 1, prevInd)

            take = 0
            if prevInd == -1 or nums[ind] < nums[prevInd]:
                take = 1 + rec(ind - 1, ind)

            DP[ind][prevInd + 1] = max(take, not_take)

            return DP[ind][prevInd + 1]

        return rec(n - 1, -1)

  
