
# https://www.geeksforgeeks.org/problems/rod-cutting0840/1

# | Approach             | Time Complexity | Space Complexity |
# | -------------------- | --------------: | ---------------: |
# | **1. Recursion**     |       **O(2ᴺ)** |         **O(N)** |
# | **2. Memoization**   |       **O(N²)** |        **O(N²)** |
# | **3. 2D Tabulation** |       **O(N²)** |        **O(N²)** |
# | **4. 1D Tabulation** |       **O(N²)** |         **O(N)** |


# class Solution:
#     def cutRod(self, price: list[int]) -> int:
#         capacity = len(price)
#         def rec(index,length):
#             if index == 0:
#                 return (length//(index+1))*price[index]
#             not_take = rec(index-1,length)
#             take = 0
#             if index+1<=length:
#                 take = price[index]+rec(index,length-(index+1))
#             return max(take,not_take)
#         return rec(len(price)-1,capacity)
# class Solution:
#     def cutRod(self, price: list[int]) -> int:
#         capacity = len(price)
#         DP = [[-1]*(capacity+1) for _ in range(len(price))]
#         def rec(index,length):
#             if DP[index][length]!=-1:
#                 return DP[index][length]
#             if index == 0:
#                 return (length//(index+1))*price[index]
#             not_take = rec(index-1,length)
#             take = 0
#             if index+1<=length:
#                 take = price[index]+rec(index,length-(index+1))
#             DP[index][length] = max(take,not_take)
#             return DP[index][length]
#         return rec(len(price)-1,capacity)

# class Solution:
#     def cutRod(self, price: list[int]) -> int:
#         capacity = len(price)
#         DP = [[0]*(capacity+1) for _ in range(len(price))]
#         for weight in range(1,capacity+1):
#             DP[0][weight] = (weight//1)*price[0]
#         for index in range(1,len(price)):
#             for weight in range(1,capacity+1):
#                 not_take = DP[index-1][weight]
#                 take = 0
#                 if index+1<=weight:
#                     take = price[index]+DP[index][weight-(index+1)]
#                 DP[index][weight] = max(take,not_take)
#         return DP[len(price)-1][capacity]

class Solution:
    def cutRod(self, price: list[int]) -> int:
        capacity = len(price)
        DP = [0]*(capacity+1)
        for weight in range(1,capacity+1):
            DP[weight] = (weight//1)*price[0]
        for index in range(1,len(price)):
            for weight in range(1,capacity+1):
                not_take = DP[weight]
                take = 0
                if index+1<=weight:
                    take = price[index]+DP[weight-(index+1)]
                DP[weight] = max(take,not_take)
        return DP[capacity]
