# 2099. Find Subsequence of Length K With the Largest Sum

# TC: O(nlogn) SC: O(k)
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq =[]
        for i,val in enumerate(nums):
            heapq.heappush(pq,(val,i))
            if len(pq)>k:
                heapq.heappop(pq)
        pq.sort(key = lambda x:x[1])
        return [i[0] for i in pq]
