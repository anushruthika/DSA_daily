# 2357. Make Array Zero by Subtracting Equal Amounts
# TC: O(nlogn) sc:O(1)
import heapq
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        heapq.heapify(nums)
        while any(nums):
            x = heapq.heappop(nums)
            while any(nums) and x==0:
                x = heapq.heappop(nums)
            for i in range(len(nums)):
                nums[i]=nums[i]-x
            count+=1
        return count
        
