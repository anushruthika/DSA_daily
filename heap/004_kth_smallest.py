import heapq
class Solution:
    def kthSmallest(self, arr, k):
        pq = []
        for i in arr:
            heapq.heappush(pq,-1*i)
            if len(pq)>k:
                heapq.heappop(pq)
        return -1*pq[0]
