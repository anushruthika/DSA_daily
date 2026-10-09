# 79. Word Search

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(word)
        lr = len(board)
        lc = len(board[0])
        if n>lr*lc:
            return False
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c,i):
            # print(board[r][c],word[i],r,c,i)
            if i+1 == n:
                return True
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0<=nr<lr and 0<=nc<lc and (nr,nc) not in visited and board[nr][nc] == word[i+1]:
                    visited.add((nr,nc))
                    if dfs(nr,nc,i+1):
                        visited.remove((nr,nc))
                        return True
                    visited.remove((nr,nc))
        for r in range(lr):
            for c in range(lc):
                
                if board[r][c]==word[0]:
                    visited.add((r,c))
                    if dfs(r,c,0):
                        return True
                    visited.remove((r,c))
        return False
