
# TC:  O(n+klogn) SC: O(n)
# 2558. Take Gifts From the Richest Pile

import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-1*i for i in gifts]
        heapq.heapify(gifts)
        s=0
        for _ in range(k):
            heapq.heappush(gifts,-1*(math.floor((heapq.heappop(gifts)*-1)**0.5)))
        return -1*sum(gifts)
