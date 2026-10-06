# 55. Jump Game

# O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return True
            # return 0
        left = 0
        right = 0
        maxInd = 0
        steps = 0
        while left<=n and left<=right:
            if maxInd>=n-1:
                return True
                # return steps
            for i in range(left,right+1):
                maxInd = max(maxInd,i+nums[i])
            left = right+1
            right = maxInd
            steps+=1
        return False




############### BRUTE FORCE
# TC: O(2^n) (exponential)
# SC: O(n) recursion stack

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(ind):

            if ind >= len(nums) - 1:
                return True

            for jump in range(1, nums[ind] + 1):
                if dfs(ind + jump):
                    return True

            return False

        return dfs(0)
        



######################## MEMOTISATION DP needed to be added




# TC: O(n)
# Each index is visited at most once.
# The while loop increments i from 0 to n-1.

# SC: O(1)
# Only uses maxInd, i, and n.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxInd = 0
        i = 0
        n = len(nums)
        while maxInd>=i and i<n:
            if maxInd>=n-1:
                return True
            maxInd = max(maxInd,i+nums[i])
            # print(maxInd, i+nums[i],i)
            i+=1
        return False
            
    
