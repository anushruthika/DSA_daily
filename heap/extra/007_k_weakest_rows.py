# 1337. The K Weakest Rows in a Matrix
TC:O(nlogn) n>k
SC:O(n)
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = []
        for i,val in enumerate(mat):
            heapq.heappush(pq,[sum(val),i])
        l =[]
        for i in range(k):
            l.append(heapq.heappop(pq)[1])
        return l
