# Time: O(m * n) => traverse grid (marking + BFS + final conversion), each cell processed at most once
# Space: O(m * n) => queue in worst case can store many cells (boundary-connected 'O's)
# 130. Surrounded Regions

### 
# MULTI SOURCE BFS
####
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir_ = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        lr = len(board)
        lc = len(board[0])
        for i in range(lr):
            for j in range(lc):
                if board[i][j]=='O' and (i==0 or i==lr-1 or j==0 or j==lc-1):
                    queue.append((i,j))
                elif board[i][j] == 'O':
                    board[i][j] = '-'
        while queue:
            r,c = queue.popleft()
            for dr,dc in dir_:
                nr,nc = r+dr,c+dc 
                if 0<=nr<lr and 0<=nc<lc:
                    if board[nr][nc]== '-':
                        board[nr][nc] = 'O'
                        queue.append((nr,nc))
        for i in range(lr):
            for j in range(lc):
                if board[i][j]=='-':
                    board[i][j] ='X'


# multi source dfs:

# Time: O(m * n) => full grid traversal (marking) + DFS traversal (each cell visited at most once) + final pass
# Space: O(m * n) => recursion stack in worst case (grid fully connected), best O(1) to O(log n) depending on shape

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lr = len(board)
        lc = len(board[0])
        arr = []
        for i in range(lr):
            for j in range(lc):
                if board[i][j]=='O':
                    board[i][j] = '-'
                    if (i==0 or i==lr-1 or j==0 or j==lc-1):
                        arr.append((i,j))
                    
        def flood_fill(nr,nc):
            if not(0<=nr<lr and 0<=nc<lc) or board[nr][nc]!= '-':
                return
            board[nr][nc] = 'O'
            flood_fill(nr+1,nc)
            flood_fill(nr-1,nc)
            flood_fill(nr,nc+1)
            flood_fill(nr,nc-1)
        for i,j in arr:
            flood_fill(i,j)
        for i in range(lr):
            for j in range(lc):
                if board[i][j]=='-':
                    board[i][j] ='X'
