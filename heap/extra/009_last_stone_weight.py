# 1046. Last Stone Weight
# TC: o(nlogn) SC: O(n)
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i in range(len(stones)):
            if stones[i]>0:
                heapq.heappush(pq,-1*stones[i])
        while len(pq)>=2:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if -1*(x-y)>0:
                heapq.heappush(pq,x-y)
        return pq[0]*-1 if len(pq)>0 else 0
