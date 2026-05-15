# 2149. Rearrange Array Elements by Sign
# TC: o(n) SC: O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        # place + first then -
        n,p = 1,0
        for num in nums:
            if num<0:
                res[n] = num
                n+=2
            else:
                res[p]=num
                p+=2
        return res
