# 506. Relative Ranks
# TC: O(nlogn) SC:O(n)
import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pq = []
        for i,val in enumerate(score):
            heapq.heappush(pq,[-1*val,i])
        m = len(score)
        # form rank
        rank = ["Gold Medal","Silver Medal","Bronze Medal"]
        i=3
        while i<m:
            rank.append(f"{i+1}")
            i+=1
        res=[0]*m
        i=0
        while len(pq):
            val,ind = heapq.heappop(pq)
            res[ind]=rank[i]
            i+=1
        return res
        
              
