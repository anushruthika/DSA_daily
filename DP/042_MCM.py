from functools import lru_cache
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        N = len(arr)
        @lru_cache(None)
        def dfs(i,j):
            if i == j:
                return 0
            cost = float('inf')
            for k in range(i,j):
                cost=min(cost, (arr[i-1]*arr[k]*arr[j])+ dfs(i,k) +dfs(k+1,j))
            return cost
        return dfs(1,N-1)
        
