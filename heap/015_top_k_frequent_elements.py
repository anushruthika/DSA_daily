# 347. Top K Frequent Elements
# TC:O(nlogk) SC: o(k+n)
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i]+=1
        pq = []
        for i in count:
            heapq.heappush(pq,(count[i],i))
            if len(pq)>k:
                heapq.heappop(pq)
        return [i for v,i in pq]
