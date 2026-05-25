# https://www.geeksforgeeks.org/problems/maximum-sum-combination/1
# TC: O(k log k)
# SC: O(k)
import heapq
class Solution:
    def topKSumPairs(self, a, b, k):
        # a & b equal size 
        n = len(a)
        # sort descending
        a.sort(reverse=True)
        b.sort(reverse=True)
        pq = []
        # largest possible combination
        heapq.heappush(pq,(-(a[0]+b[0]),0,0))
        visited = set()
        visited.add((0,0))
        res = []
        while k>0:
            s,i,j = heapq.heappop(pq)
            res.append(-s)
            if i+1<n and (i+1,j) not in visited:
                heapq.heappush(pq,(-(a[i+1]+b[j]),i+1,j))
                visited.add((i+1,j))
            if j+1<n and (i,j+1) not in visited:
                heapq.heappush(pq,(-(a[i]+b[j+1]),i,j+1))
                visited.add((i,j+1))
            k-=1
        return res
