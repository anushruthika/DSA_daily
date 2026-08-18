# 120. Triangle

# | Approach                          | Time Complexity | Space Complexity | Why                                                                                          |
# | --------------------------------- | --------------: | ---------------: | -------------------------------------------------------------------------------------------- |
# | **1. Recursion**                  |       **O(2ⁿ)** |         **O(n)** | Each position has **2 choices** (`ind` or `ind+1`), and recursion depth is `n`.              |
# | **2. Memoization**                |       **O(n²)** |        **O(n²)** | There are `1+2+...+n = n(n+1)/2 = O(n²)` unique `(row, ind)` states, and each state is calculated once. |
# | **3. Tabulation**                 |       **O(n²)** |        **O(n²)** | We calculate every element of the triangle once. The DP table stores all `O(n²)` elements.   |
# | **4. Space-optimized Tabulation** |       **O(n²)** |         **O(n)** | We still process all `O(n²)` triangle elements, but keep only one DP array of size `n`.      |

class Solution:
    # recursion
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     def rec(ind,row):
    #         if row==n-1:
    #             return triangle[row][ind]
    #         return min(rec(ind+1,row+1),rec(ind,row+1))+triangle[row][ind]
    #     return rec(0,0)
    # # memoization
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     DP = {}
    #     def rec(ind,row):
    #         if (ind,row) in DP:
    #             return DP[(ind,row)]
    #         if row==n-1:
    #             return triangle[row][ind]
    #         DP[(ind,row)] = min(rec(ind+1,row+1),rec(ind,row+1))+triangle[row][ind]
    #         return DP[(ind,row)]
    #     return rec(0,0)
    # # tabulation
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     DP = [[] for i in range(n)]
    #     DP[0] = [triangle[0][0]]
    #     for row in range(1,n):
    #         for ind in range(0,row+1):
    #             if ind==0:
    #                 DP[row].append(DP[row-1][ind]+triangle[row][ind])
    #             elif ind == row:
    #                 DP[row].append(DP[row-1][ind-1]+triangle[row][ind])
    #             else:
    #                 DP[row].append(min(DP[row-1][ind-1],DP[row-1][ind])+triangle[row][ind])
    #     return min(DP[-1])
    # space reduction
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        DP = [triangle[0][0]]
        for row in range(1,n):
            #  necessary to update it in reverse, as you can update.
            # for ind in range(0,row+1):
            for ind in range(row,-1,-1):
                if ind==0:
                    DP[ind] = DP[ind]+triangle[row][ind]
                elif ind == row:
                    DP.append(DP[ind-1]+triangle[row][ind])
                else:
                    DP[ind] = min(DP[ind-1],DP[ind])+triangle[row][ind]
        return min(DP)
    


