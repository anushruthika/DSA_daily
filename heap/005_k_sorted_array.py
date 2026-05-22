# https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1

# TC: O(nlogn+nk) SC: o(n)

import heapq

class Solution:
    def isKSortedArray(self, arr, n, k):

        temp = arr[:]
        # Create min heap
        heapq.heapify(temp)
        for i in range(n):
            smallest = heapq.heappop(temp)
            start = max(0, i-k)
            end = min(n, i+k+1)
            found = False
            for j in range(start, end):

                if arr[j] == smallest:
                    found = True
                    break

            if not found:
                return "No"

        return "Yes"
