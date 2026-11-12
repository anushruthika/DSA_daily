# 1031. Maximum Sum of Two Non-Overlapping Subarrays

from functools import lru_cache
class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstlen: int, secondlen: int) -> int:
        if firstlen>secondlen:
            firstlen,secondlen = secondlen,firstlen
        n = len(nums)
        @lru_cache(None)
        def rec(ind,f,s):
            if ind >= n:
                return 0
            if f==0 and s == 0:
                return 0
            take_first = float('-inf')
            if f!=0:
                take_first = sum(nums[ind:ind+firstlen])+rec(ind+firstlen,0,s)
            take_second = float('-inf')
            if s!=0:
                take_second = sum(nums[ind:ind+secondlen])+rec(ind+secondlen,f,0)
            not_take = rec(ind+1,f,s)
            return max(take_first,take_second,not_take)
        return rec(0,firstlen,secondlen)
        
        
            
