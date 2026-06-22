# 45. Jump Game II

# TC: O(2^n) (exponential)
# SC: O(n) recursion stack
############## BRUTE FORCE - DFS Recursion
class Solution:
    def jump(self, nums: List[int]) -> int:

        def dfs(i):

            if i >= len(nums) - 1:
                return 0

            ans = float('inf')

            for jump in range(1, nums[i] + 1):
                ans = min(ans, 1 + dfs(i + jump))

            return ans

        return dfs(0)

############ MEMOTISATION
# TC: O(n^2)
# SC: O(n)


################### SOLUTION NEEDED TO BE POSTED


############# GREEDY (OPTIMAL)
# TC: O(n)
# SC: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        jumps = 0
        while r<n-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, nums[i]+i)
            l = r+1
            jumps+=1
            r = farthest
        return jumps
