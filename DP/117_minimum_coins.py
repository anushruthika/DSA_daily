# https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

# | Approach          |             Time |   Space | Why                                                |
# | ----------------- | ---------------: | ------: | -------------------------------------------------- |
# | **Recursion**     | `O(2^N)` approx. |  `O(N)` | Repeatedly explores take/not-take branches         |
# | **Memoization**   |          `O(MN)` | `O(MN)` | Each `(index,target)` state calculated once        |
# | **2D Tabulation** |          `O(MN)` | `O(MN)` | Calculates every DP state iteratively              |
# | **1D Tabulation** |          `O(MN)` |  `O(N)` | Same states, but removes redundant index dimension |


# class Solution:
#     def findMin(self, n: int) -> int:
#         arr = [1,2,5,10]
#         def rec(index,target):
#             if target == 0:
#                 return 0
#             if index < 0:
#                 return float('inf')
#             not_take = rec(index-1,target)
#             take = float('inf')
#             if arr[index]<=target:
#                 take = 1+rec(index,target-arr[index])
#             return min(not_take,take)
#         return rec(3,n)
# class Solution:
#     def findMin(self, n: int) -> int:
#         arr = [1,2,5,10]
#         DP = [[-1]*(n+1) for i in range(len(arr))]
#         def rec(index,target):
#             if target == 0:
#                 return 0
#             if index < 0:
#                 return float('inf')
#             if DP[index][target] != -1:
#                 return DP[index][target]
#             not_take = rec(index-1,target)
#             take = float('inf')
#             if arr[index]<=target:
#                 take = 1+rec(index,target-arr[index])
#             DP[index][target] = min(not_take,take)
#             return DP[index][target]
#         return rec(3,n)

# class Solution:
#     def findMin(self, n: int) -> int:
#         arr = [1,2,5,10]
#         DP = [[float('inf')] * (n + 1) for _ in range(len(arr))]
#         # eg: arr = [0] n = 0 0 ways
#         DP[0][0] = 0
#         for index in range(len(arr)):
#             DP[index][0] = 0
#         for target in range(1, n + 1):
#             if target % arr[0] == 0:
#                 DP[0][target] = target // arr[0]
            
#         for index in range(1,len(arr)):
#             for target in range(1,n+1):
#                 not_take = DP[index-1][target]
#                 take = float('inf')
#                 if arr[index]<=target:
#                     take = 1+DP[index][target-arr[index]]
#                 DP[index][target] = min(take,not_take)
#         if DP[len(arr)-1][n]!= -1:
#             return DP[len(arr)-1][n]
#         else:
#             return -1

class Solution:
    def findMin(self, n: int) -> int:
        arr = [1,2,5,10]
        DP = [float('inf')] * (n + 1)
        # eg: arr = [0] n = 0 0 ways
        DP[0] = 0
        for target in range(1, n + 1):
            if target % arr[0] == 0:
                DP[target] = target // arr[0]
            
        for index in range(1,len(arr)):
            for target in range(1,n+1):
                not_take = DP[target]
                take = float('inf')
                if arr[index]<=target:
                    take = 1+DP[target-arr[index]]
                DP[target] = min(take,not_take)
        if DP[n]!= -1:
            return DP[n]
        else:
            return -1
                

                   
               
           
