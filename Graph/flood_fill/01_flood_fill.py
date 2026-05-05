# 733. Flood Fill

# Time: O(m * n) => each cell is visited at most once
# Space: O(m * n) => queue can hold up to all cells in worst case

from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rl = len(image)
        cl = len(image[0])
        queue = deque([(sr,sc)])
        org = image[sr][sc]
        if org == color:
            return image
        image[sr][sc] = color
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            nr,nc = queue.popleft()
            for dr,dc in directions:
                r,c = nr+dr,nc+dc
                if 0<=r<rl and 0<=c<cl and image[r][c] == org:
                    image[r][c] = color
                    queue.append((r,c))
        return image

#####
# DFS
#####
# Time: O(m * n) => each cell is visited at most once
# Space: O(m * n) => recursion stack in worst case (grid fully connected), best O(1) to O(log n) depending on shape
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org = image[sr][sc]
        def flood_fill(x,y):
            # if not (0<=x<m and 0<=y<n and image[x][y] == prev_color):
            if (x < 0 or x >= len(image)) or (y < 0 or y >= len(image[0])) or (image[x][y] == color) or (image[x][y] != org): 
                return
            image[x][y] = color
            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)
        if org!=color:
            flood_fill(sr, sc)
        return image
