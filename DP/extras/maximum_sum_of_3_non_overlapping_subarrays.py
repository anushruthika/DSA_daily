# 689. Maximum Sum of 3 Non-Overlapping Subarrays

from functools import lru_cache

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        n = len(nums)

        arr = []
        for i in range(n-K+1):
            arr.append(sum(nums[i:i+K]))

        L = 3

        @lru_cache(None)
        def rec(ind, length):

            if length == 0:
                return (0, ())

            if ind < 0:
                return (float('-inf'), ())

            # Take
            prev_sum, prev_indices = rec(ind-K, length-1)
            take = (prev_sum + arr[ind], prev_indices + (ind,))

            # Not take
            not_take = rec(ind-1, length)

            # Maximize sum; on ties, choose lexicographically
            # smallest indices
            if take[0] > not_take[0]:
                return take
            elif take[0] < not_take[0]:
                return not_take
            else:
                return min(take, not_take, key=lambda x: x[1])

        return list(rec(len(arr)-1, L)[1])
