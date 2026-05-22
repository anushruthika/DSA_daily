# 1464. Maximum Product of Two Elements in an Array
# TC: O(nlogn) SC: O(n)
import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pq =[]
        for i in nums:
            heapq.heappush(pq,-1*i)
        return ((-1*heapq.heappop(pq))-1) * ((-1*heapq.heappop(pq))-1)
