# 2441. Largest Positive Integer That Exists With Its Negative
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for i in nums:
            if -i in s:
               ans = max(ans,abs(i)) 
        return ans
        
# Time Complexity: O(n log n) (sorting)
# Space Complexity: O(n)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        nums.sort()
        max_now = -1
        for num in nums:
            if (-1*num) not in s:
                s.add(num)
            if -1*num in s:
                max_now = num
        return max_now


        
