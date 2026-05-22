# 2335. Minimum Amount of Time to Fill Cups
# TC: O(1) => O(nlogn+2*countlog(n)) => n=3, O(count) or simply O(1) 
# SC: O(1) => o(n) n=3 since,o(1)
import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        pq = []

        for i in amount:
            if i>0:
                heapq.heappush(pq,-1*i)
        count =0
        while len(pq)>0:
            if len(pq)>=2:
                x = heapq.heappop(pq)
                y = heapq.heappop(pq)
                if x+1 <0:
                    heapq.heappush(pq,x+1)
                if y+1 <0:
                    heapq.heappush(pq,y+1)
            else:
                x = heapq.heappop(pq)
                if x+1 <0:
                    heapq.heappush(pq,x+1)
            count+=1
        return count
