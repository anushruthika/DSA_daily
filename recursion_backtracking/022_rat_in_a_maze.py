# https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        n = len(maze)
        directions = [(0,1,'R'),(1,0,'D'),(0,-1,'L'),(-1,0,'U')]
        if maze[0][0]==0 or maze[n-1][n-1] == 0:
            return []
        visited = set()
        # use list because order of storing directions is important 
        # and we also getting duplicate 'R' 'D'.. thus set will remove the duplicates 
        # and will hit value not found error
        
        ans_d = list()
        res = []
        def dfs(r,c):
            if r == n-1 and c == n-1:
                res.append("".join(ans_d))
                return
            visited.add((r,c))
            for dr,dc,di in directions:
                nr,nc = dr+r,dc+c
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited and maze[nr][nc]==1:
                    ans_d.append(di)
                    dfs(nr,nc)
                    ans_d.pop()
            visited.remove((r,c))
        dfs(0,0)
        return sorted(res)
            
