# https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1

# n = number of elements in arr
# S = target_sum = (sum(arr) + diff) / 2
# | Approach            |         Time |        Space | Why                                                                  |
# | ------------------- | -----------: | -----------: | -------------------------------------------------------------------- |
# | **Recursion**       |    **O(2ⁿ)** |     **O(n)** | Each element has 2 choices: take / not take. Recursion depth is `n`. |
# | **Memoization**     | **O(n × S)** | **O(n × S)** | There are `n × S` `(index, target)` states, each calculated once.    |
# | **Tabulation**      | **O(n × S)** | **O(n × S)** | You fill an `n × S` DP table, with O(1) work per cell.               |
# | **Space optimized** | **O(n × S)** |     **O(S)** | Only one row of `S` states is maintained.                            |

# S1 + S2 = total
# S1 - S2 = diff
# 2 × S1 = total + diff # Add eqns
# S1 = (total + diff) / 2
# class Solution:
#     def countPartitions(self, arr, diff):
#         n = len(arr)
#         target_sum = sum(arr)+diff
#         if target_sum % 2 !=0:
#             return 0
#         target_sum//=2
#         def rec(index,target):
#             if index == 0:
#                 if target == 0 and arr[0] == 0:
#                     return 2
#                 if target == 0 or arr[0]==target:
#                     return 1
#                 return 0
#             not_take = rec(index-1,target)
#             take = 0
#             if arr[index]<=target:
#                 take = rec(index-1,target-arr[index])
#             return take+not_take
#         return rec(n-1,target_sum)
# class Solution:
#     def countPartitions(self, arr, diff):
#         n = len(arr)
#         target_sum = sum(arr)+diff
#         if target_sum % 2 !=0:
#             return 0
#         target_sum//=2
#         DP = [[-1]*(target_sum+1) for _ in range(n)]
#         def rec(index,target):
#             if DP[index][target] != -1:
#                 return DP[index][target]
#             if index == 0:
#                 if target == 0 and arr[0] == 0:
#                     return 2
#                 if target == 0 or arr[0]==target:
#                     return 1
#                 return 0
#             not_take = rec(index-1,target)
#             take = 0
#             if arr[index]<=target:
#                 take = rec(index-1,target-arr[index])
#             DP[index][target] = take+not_take
#             return DP[index][target]
#         return rec(n-1,target_sum)
# class Solution:
#     def countPartitions(self, arr, diff):
#         n = len(arr)
#         target_sum = sum(arr)+diff
#         if target_sum % 2 !=0:
#             return 0
#         target_sum//=2
#         DP = [[0]*(target_sum+1) for _ in range(n)]
#         if arr[0] == 0:
#             DP[0][0] = 2
#         else:
#             DP[0][0] = 1
#         if arr[0]!=0 and arr[0]<=target_sum:
#             DP[0][arr[0]] = 1
#         for index in range(1,n):
#             for target in range(target_sum+1):
#                 not_take = DP[index-1][target]
#                 take = 0
#                 if arr[index]<=target:
#                     take = DP[index-1][target-arr[index]]
#                 DP[index][target] = not_take+take
#         return DP[n-1][target_sum]

class Solution:
    def countPartitions(self, arr, diff):
        n = len(arr)
        target_sum = sum(arr)+diff
        if target_sum % 2 !=0:
            return 0
        target_sum//=2
        DP = [0]*(target_sum+1)
        if arr[0] == 0:
            DP[0] = 2
        else:
            DP[0] = 1
        if arr[0]!=0 and arr[0]<=target_sum:
            DP[arr[0]] = 1
        for index in range(1,n):
            # for target in range(target_sum+1):
            for target in range(target_sum,-1,-1):
                not_take = DP[target]
                take = 0
                if arr[index]<=target:
                    take = DP[target-arr[index]]
                DP[target] = not_take+take
        return DP[target_sum]
