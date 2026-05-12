# time: O(n) space: O(1)
class Solution(object):
    def singleNumber(self, nums):

        sum = 0

        # X ^ X = 0
        # 0 ^ X = X

        for i in range(0, len(nums)):
            sum ^= nums[i]

        return sum
