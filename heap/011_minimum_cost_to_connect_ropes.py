# https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
# TC: o(nlogn) SC: O(n)
import heapq
class Solution:
   def minCost(self, arr):
    heapq.heapify(arr)
    s = 0
    while len(arr)>=2:
        n1 = heapq.heappop(arr)
        n2 = heapq.heappop(arr)
        heapq.heappush(arr,n1+n2)
        s +=n1+n2
    return s
