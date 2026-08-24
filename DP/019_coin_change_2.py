# 518. Coin Change II

# N = len(coins)
# A = amount
# | Approach             |  Time Complexity |                Space Complexity |
# | -------------------- | ---------------: | ------------------------------: |
# | **1. Recursion**     | **O(2^(N + A))** |                    **O(N + A)** |
# | **2. Memoization**   |     **O(N × A)** | **O(N × A + N + A) → O(N × A)** |
# | **3. 2D Tabulation** |     **O(N × A)** |                    **O(N × A)** |
# | **4. 1D Tabulation** |     **O(N × A)** |                        **O(A)** |

# infinite coins in this denomination
# #                   rec(2,5)
#                     /       \
#                 rec(1,5)    rec(2,0)+1
#                /      \
#          rec(0,5)+1   rec(1,3)
#                   /       \
#               rec(0,3)+1 rec(1,1)
#                           / \
#                    rec(0,1)+1  Xrec(1,-1)

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         def rec(index,target):
#             if target == 0:
#                 return 1
#             if index == 0:
#                 if target%coins[0]==0:
#                     return 1
#                 return 0
#             not_take = rec(index-1,target)
#             take = 0
#             if target>=coins[index]:
#                 take = rec(index,target-coins[index])
#             return not_take+take
#         return rec(len(coins)-1,amount)

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         DP = [[-1]*(amount+1) for _ in range(len(coins))]
#         def rec(index,target):
#             if DP[index][target]!=-1:
#                 return DP[index][target]
#             if target == 0:
#                 return 1
#             if index == 0:
#                 if target%coins[0]==0:
#                     return 1
#                 return 0
#             not_take = rec(index-1,target)
#             take = 0
#             if target>=coins[index]:
#                 take = rec(index,target-coins[index])
#             DP[index][target] = not_take+take
#             return DP[index][target]
#         return rec(len(coins)-1,amount)

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         DP = [[-1]*(amount+1) for _ in range(len(coins))]
#         def rec(index,target):
#             if DP[index][target]!=-1:
#                 return DP[index][target]
#             if target == 0:
#                 return 1
#             if index == 0:
#                 if target%coins[0]==0:
#                     return 1
#                 return 0
#             not_take = rec(index-1,target)
#             take = 0
#             if target>=coins[index]:
#                 take = rec(index,target-coins[index])
#             DP[index][target] = not_take+take
#             return DP[index][target]
#         return rec(len(coins)-1,amount)
        # 0   1   2   3   4   5
# 1   0   
# 2   1
# 5   2
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         DP = [[0]*(amount+1) for _ in range(len(coins))]
#         # not possible for coins[i] to be 0
#         for possible_amount in range(amount+1):
#             if possible_amount%coins[0] == 0:
#                 DP[0][possible_amount] = 1
#         # if possible_amount is 0 then 1
#         for index in range(len(coins)):
#             DP[index][0] = 1
#         for index in range(1,len(coins)):
#             for target in range(1,amount+1):
#                 not_take = DP[index-1][target]
#                 take = 0
#                 if target>=coins[index]:
#                     take = DP[index][target-coins[index]]
#                 DP[index][target] = take+not_take
#         return DP[len(coins)-1][amount]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        DP =  [0]*(amount+1)

        # not possible for coins[i] to be 0
        for possible_amount in range(amount+1):
            if possible_amount%coins[0] == 0:
                DP[possible_amount] = 1
        # if possible_amount is 0 then 1
        DP[0] = 1
        for index in range(1,len(coins)):
            temp = [0]*(amount+1)
            for target in range(1,amount+1):
                not_take = DP[target]
                take = 0
                if target>=coins[index]:
                    take = DP[target-coins[index]]
                DP[target] = take+not_take
        return DP[amount]
