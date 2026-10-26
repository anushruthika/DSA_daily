# 2965. Find Missing and Repeated Values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        size = m*n
        freq = dict.fromkeys(list(range(1,size+1)),0)
        repeating = None
        for i in range(m):
            for j in range(n):
                freq[grid[i][j]]+=1
        for num in range(1,size+1):
            if freq[num] == 2:
                repeating = num
            if freq[num] == 0:
                missing = num
        return [repeating,missing]
