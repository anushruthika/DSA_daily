# 2974. Minimum Number Game

# TC: O(n log n)
# SC: O(n)
import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        arr =[]
        while len(nums)>=2:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            arr.extend([bob,alice])
        return arr
            
