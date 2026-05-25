# 1331. Rank Transform of an Array
# TC: O(nlogn) SC: O(n)
# edge case: same elements share same rank
import heapq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        pq = []
        for i,val in enumerate(arr):
            heapq.heappush(pq,(val,i))
        n = len(arr)
        n_set = len(set(arr))
        l = [-1]*n
        prev = float('-inf')
        prev_rank = -1
        i=1
        while pq:
            val,ind = heapq.heappop(pq)
            if val == prev:
                l[ind] = prev_rank
                continue
            l[ind] = i
            prev = val
            prev_rank = i
            i+=1
        return l
            
