# https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1

# TC:o(n) SC: O(n)
from collections import deque
class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)
        if n>0:
            queue = deque([0])
            while queue:
                ind = queue.popleft()
                node = arr[ind]
                if 2*ind+1>=n:
                    continue
                left = arr[2*ind+1]
                if node<left:
                    return False
                queue.append(2*ind+1)
                if 2*ind+2>=n:
                    continue
                right = arr[2*ind+2]
                if node<right:
                    return False
                queue.append(2*ind+2)
        return True
        
        
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
