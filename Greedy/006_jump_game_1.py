# 55. Jump Game

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
            
    
