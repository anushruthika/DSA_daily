# 3264. Final Array State After K Multiplication Operations I
# TC: O((n+k)logn) SC:O(n)
import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq =[]
        for i,val in enumerate(nums):
            heapq.heappush(pq,(val,i))
        for i in range(k):
            val,ind = heapq.heappop(pq)
            nums[ind] = nums[ind]*multiplier
            heapq.heappush(pq,(nums[ind],ind))
        return nums
