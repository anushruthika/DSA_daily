# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

# #  Recursion Tree
# arr = [1,2,3,1] target = 4
# n = len(arr) = 4 
#                             func(n-1,4)
#                  NT /                                \ T
#                 func(2,4)                           func(2,3)
#         NT /            \T                      NT /            \T
#     func(1,4)           func(1,1)           func(1,3)       func(1,0)T
#   NT/      \T         NT/      \T           NT/      \T  
# func(0,4)F f(0,2)F  f(0,1)T   f(0,-1)   f(0,3)F   f(0,1) T

# n = number of elements in arr
# S = target sum

# | Approach                  | Time Complexity | Space Complexity | Reason                                                                                           |
# | ------------------------- | --------------: | ---------------: | ------------------------------------------------------------------------------------------------ |
# | **1. Recursion**          |       **O(2ⁿ)** |         **O(n)** | At every element, there are 2 choices: **take** or **not take**. Maximum recursion depth is `n`. |
# | **2. Memoization**        |    **O(n × S)** |     **O(n × S)** | State is `(index, target)`. There are `n × S` possible states, and each state does O(1) work.    |
# | **3. Tabulation**         |    **O(n × S)** |     **O(n × S)** | The DP table has `n × (S+1)` cells, and each cell is calculated once.                            |
# | **4. Space-optimized DP** |    **O(n × S)** |         **O(S)** | We only keep one row of the DP table. For each element, we process all `S` targets.              |


#  Recursion

# class Solution:
#     def isSubsetSum(self, arr: list[int], sum: int) -> bool:
#         def rec(index,target):
#             if target == 0:
#                 return True
#             if index == 0:
#                 return arr[0] == target
#             not_take = rec(index-1,target)
#             take = False
#             if target>=arr[index]:
#                 take = rec(index-1,target-arr[index])
#             return not_take or take
#         return rec(len(arr)-1,sum)
        
# # Memoization
# class Solution:
#     def isSubsetSum(self, arr: list[int], sum: int) -> bool:
#         n = len(arr)
#         DP = [[-1]*(sum+1) for _ in range(n) ]
#         def rec(index,target):
#             if DP[index][target] != -1:
#                 return DP[index][target] 
#             if target == 0:
#                 return True
#             if index == 0:
#                 return arr[0] == target
#             not_take = rec(index-1,target)
#             take = False
#             if target>=arr[index]:
#                 take = rec(index-1,target-arr[index])
#             DP[index][target] = not_take or take
#             return DP[index][target]
#         return rec(n-1,sum)

# # Tabulation
# class Solution:
#     def isSubsetSum(self, arr: list[int], sum: int) -> bool:
#         n = len(arr)
#         DP = [[False]*(sum+1) for _ in range(n) ]
#         for ind in range(n):
#             DP[ind][0] = True
#         # edge case: arr = [7 4 5] sum = 2 
#         # if no if case then index out of bound error
#         if arr[0] <= sum:
#             DP[0][arr[0]] = True
#         for ind in range(1,n):
#             for target in range(1,sum+1):
#                 not_take = DP[ind-1][target]
#                 take = False
#                 if target>=arr[ind]:
#                     take = DP[ind-1][target-arr[ind]]
#                 DP[ind][target] = take or not_take
#         return DP[n-1][sum]

# Space complexity reduction
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        n = len(arr)
        DP = [True]+[False]*(sum)
        # edge case: arr = [7 4 5] sum = 2 
        # if no if case then index out of bound error
        if arr[0] <= sum:
            DP[arr[0]] = True
        
        for ind in range(1,n):
            # Traverse backwards not lose previous DP record
            for target in range(sum, 0, -1):
                not_take = DP[target]
                take = False
                if target>=arr[ind]:
                    take = DP[target-arr[ind]]
                DP[target] = take or not_take
        return DP[sum]
        

    
    
    
    
    
    
    
    
        
