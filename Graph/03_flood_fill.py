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
      
