# 198. House Robber
#  Maximum sum of non adjacent elements


# DP[index] = max(DP[index-1], nums[index]+DP[index-2])


# | Approach               | Time Complexity | Space Complexity | Why                                                                       |
# | ---------------------- | --------------: | ---------------: | ------------------------------------------------------------------------- |
# | **1. Recursion**       |       **O(2ⁿ)** |         **O(n)** | Each state branches into `i-1` and `i-2`; recursion stack can go `n` deep |
# | **2. Memoization**     |        **O(n)** |         **O(n)** | Each `index` is calculated only once; DP array + recursion stack          |
# | **3. Tabulation**      |        **O(n)** |         **O(n)** | One loop through `n` houses; DP array stores all states                   |
# | **4. Space Optimized** |        **O(n)** |         **O(1)** | One loop; only `prev1`, `prev2`, and `cur` are needed                     |

  
#  logic: f(i) = max( nums[i] + f(i+2), f(i+1))
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def rec(index):
#             if index == 0:
#                 return nums[0]
#             if index == 1:
#                 return max(nums[0],nums[1])
#             return max(rec(index-1),nums[index]+rec(index-2))
#         return rec(len(nums)-1)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         DP = [-1]*n
#         DP[0] = nums[0]
#         if n == 1:
#             return DP[0]
#         DP[1] = max(nums[0],nums[1])
#         if n ==2:
#             return DP[1]
#         def rec(index):
#             if DP[index-1]==-1:
#                 DP[index-1] = rec(index-1)
#             if DP[index-2]== -1:
#                 DP[index-2] = rec(index-2)
#             return max(DP[index-1],nums[index]+DP[index-2])
#         return rec(n-1)

# Tabulation 
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         DP = [-1]*n
#         DP[0] = nums[0]
#         if n == 1:
#             return DP[0]
#         DP[1] = max(nums[0],nums[1])
#         if n ==2:
#             return DP[1]
#         for index in range(2,n):
#             DP[index] = max(DP[index-1],nums[index]+DP[index-2])
#         return  DP[n-1]

# Space complexity
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev1 = nums[0]
        if n == 1:
            return prev1
        prev2 = max(nums[0],nums[1])
        if n ==2:
            return prev2
        for index in range(2,n):
            cur = max(prev2,nums[index]+prev1)
            prev1 = prev2
            prev2 = cur
        return  prev2


