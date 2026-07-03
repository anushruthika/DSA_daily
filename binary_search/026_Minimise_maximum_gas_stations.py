

######## BRUTE FORCE
# Time: O(k × n)
# For each of the k gas stations, you scan all n-1 segments.
# Space: O(n)
# The section array stores the number of extra gas stations placed in each segment.
# HIT TLE

class Solution:
    def minMaxDist(self, arr, k):
        n = len(arr)
        if n<= 1:
            return 0
        section = [0]*(n-1)
        for i in range(k):
            max_tracker = -1
            max_ind = -1
            for i in range(n-1):
                dif = arr[i+1]-arr[i]
                cur_section_len = dif/(section[i]+1)
                if max_tracker<cur_section_len:
                    max_tracker = cur_section_len
                    max_ind = i
            section[max_ind]+=1
        ans = float('-inf')
        for i in range(n-1):
            sec = (arr[i+1] - arr[i]) / (section[i] + 1)
            ans = max(ans, sec)
        return ans

#### HEAP IMPLEMENTATION
# TC: O(n + k log n)
# SC: O(n)

import heapq
class Solution:
    def minMaxDist(self, arr, k):
        n = len(arr)
        if n<= 1:
            return 0
        section = [0]*(n-1)
        pq = []
        for i in range(n-1):
            heapq.heappush(pq,(-1*(arr[i+1]-arr[i]),i))
        for i in range(k):
            _,ind = heapq.heappop(pq)
            section[ind]+=1
            new_val = -1*(arr[ind+1]-arr[ind])/(section[ind]+1)
            heapq.heappush(pq,(new_val,ind))
        return -1*heapq.heappop(pq)[0]

###### BINARY SEARCH
# TC: O(n × log(maxGap / 1e-6))
# SC: O(1)
import heapq
class Solution:
    def possible(self, arr, k, dist):
        count = 0

        for i in range(len(arr) - 1):
            gap = arr[i + 1] - arr[i]

            # Number of stations needed in this gap
            count += int(gap / dist)

            # If gap is exactly divisible, one station is counted extra
            if gap % dist == 0:
                count -= 1

        return count <= k
        
    def minMaxDist(self, arr, k):
        n = len(arr)
        if n<= 1:
            return 0
        low = 0
        high = 0
        for i in range(n - 1):
            high = max(high, arr[i + 1] - arr[i])
        eps = 1e-6

        while high - low > eps:
            mid = (low + high) / 2

            if self.possible(arr, k, mid):
                high = mid
            else:
                low = mid

        return high
