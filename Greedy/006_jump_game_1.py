# 55. Jump Game

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
            
    
