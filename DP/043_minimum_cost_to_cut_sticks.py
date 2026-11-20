from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        @lru_cache(None)
        def func(i,j):
            if j == i + 1:
                return 0
            cost = float('inf')
            for num in cuts:
                if i<num<j:
                    cost  = min(cost,(j-i)+func(i,num)+func(num,j))
            if cost == float("inf"):
                return 0
            return cost
        return func(0,n)
