# 2562. Find the Array Concatenation Value
# Time Complexity: O(n)
# Reason:
# Two pointers traverse the array once.

# Space Complexity: O(1)
# Reason:
# Only constant extra variables are used.
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        j=n-1
        tot = 0
        while i<j:
            tot += int(str(nums[i])+str(nums[j]))
            i+=1
            j-=1
        if n%2 ==0:
            return tot
        else:
            return tot+nums[i]
