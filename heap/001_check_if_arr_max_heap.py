# https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1
# TC:o(nlogn) SC: O(n)
import heapq
class Solution:
    def isMaxHeap(self, arr):
        pq = []
        for i in arr:
            heapq.heappush(pq,-1*i)
        i=0
        while i<len(arr):
            if arr[i] != pq[i]*-1:
                return False
            i+=1
        return True
