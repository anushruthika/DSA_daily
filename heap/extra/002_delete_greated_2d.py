# 2500. Delete Greatest Value in Each Row

# TC: O(r⋅c⋅logc)
# SC:O(1)​
import heapq
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        s =0
        
        for arr in grid:
            heapq.heapify(arr)
        i=0
        n =len(grid[0])
        
        while i<n:
            m = float('-inf')
            # print(grid,i)
            for arr in grid:
                if arr:
                    m = max(m,heapq.heappop(arr))
            s+=m
            i+=1
            # print("--",grid)
            
        return s
