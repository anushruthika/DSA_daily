# 70. Climbing Stairs

# recursion
# 1 step: 1 way
# 2 steps: 1-1 or 2 - 2 ways fib(3)=2
# 3 steps: 1-1-1 or 1-2 or 2-1 fib(4) = 3
# Time Complexity: O(2ⁿ)
# Space = O(n) 
# class Solution:
#     def fib(self, x):
#         if x <= 1:
#             return x
#         return self.fib(x - 1) + self.fib(x - 2)
#     def climbStairs(self, n: int) -> int:
#         return self.fib(n+1)

# Dynamic Programming
# Number of ways to reach n = ways to reach n-1 + ways to reach n-2
# DP[n] = DP[n-1]+DP[n-2]


# Time Complexity: O(2ⁿ)
# Space = O(n) # recursion space , DP array space

# class Solution:
#     def fib(self, DP, x):
#         if x <= 1:
#             return x

#         if DP[x] == -1:
#             DP[x] = self.fib(DP, x - 1) + self.fib(DP, x - 2)

#         return DP[x]

#     def climbStairs(self, n: int) -> int:
#         DP = [-1] * (n + 2)
#         return self.fib(DP, n + 1)


## ITERATION
# Time: O(n)
# Space: O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         DP = [-1] * (n+2)
#         DP[0] = 0
#         DP[1] = 1
#         for i in range(2,n+2):
#             DP[i] = DP[i-1]+DP[i-2]
#         return DP[n+1]

## ITERATION
# Time: O(n)
# Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        prev1 = 0
        prev2 = 1
        for i in range(2,n+2):
            cur = prev1+prev2
            prev1 = prev2
            prev2 = cur
        return cur
