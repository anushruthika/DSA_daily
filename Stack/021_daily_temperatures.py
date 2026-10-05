# 739. Daily Temperatures

class Solution(object):
    def dailyTemperatures(self, nums):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # def nge():
        n = len(nums)
        stk = []
        res = [0]*n
        for i in range(n-1,-1,-1):
            while stk and nums[stk[-1]]<=nums[i]:
                stk.pop()
            if stk:
                res[i] = stk[-1]-i
            stk.append(i)
        return res
