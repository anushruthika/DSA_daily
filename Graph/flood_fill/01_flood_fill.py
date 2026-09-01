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
        lr = len(image)
        lc = len(image[0])
        org_color = image[sr][sc]
        if org_color == color:
            return image
        def dfs(x,y):
            if not (0<=x<lr and 0<=y<lc and image[x][y]== org_color):
                return
            image[x][y] = color
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1) 
        dfs(sr,sc)
        return image
