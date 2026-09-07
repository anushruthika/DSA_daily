# # # 4 State recursion

# class Solution:
#     def cherryPickup(self, grid):
#         n = len(grid) 
#         def rec(r1,c1,r2,c2):
#             if r1 == n-1 and c1== n-1:
#                 # it is understood that r2 == n-1 and c2 == n-1
#                 return grid[r1][c1]
#             cur_cherry = 0
#             if not (0<=r1<n and 0<=r2<n and 0<=c1<n and 0<=c2<n and grid[r1][c1]!=-1 and grid[r2][c2]!=-1):
#                 return float('-inf')
#             cur_cherry = 0
#             if r1==r2 and c1 == c2:
#                 cur_cherry = grid[r1][c1]
#             else:
#                 cur_cherry = grid[r1][c1]+grid[r2][c2]
#             best = max( rec(r1+1,c1,r2,c2+1),rec(r1,c1+1,r2,c2+1),rec(r1+1,c1,r2+1,c2),rec(r1,c1+1,r2+1,c2))
#             return best+cur_cherry
#         return max(0,rec(0,0,0,0))


# # # 3 State DP

# class Solution:
#     def cherryPickup(self, grid):
#         n = len(grid) 
#         def rec(r1,c1,r2):
#             c2 = r1+c1 - r2
#             if r1 == n-1 and c1== n-1:
#                 # it is understood that r2 == n-1 and c2 == n-1
#                 return grid[r1][c1]
#             cur_cherry = 0
#             if not (0<=r1<n and 0<=r2<n and 0<=c1<n and 0<=c2<n and grid[r1][c1]!=-1 and grid[r2][c2]!=-1):
#                 return float('-inf')
#             cur_cherry = 0
#             if r1==r2 and c1 == c2:
#                 cur_cherry = grid[r1][c1]
#             else:
#                 cur_cherry = grid[r1][c1]+grid[r2][c2]
#             best = max( rec(r1+1,c1,r2),rec(r1,c1+1,r2),rec(r1+1,c1,r2+1),rec(r1,c1+1,r2+1))
#             return best+cur_cherry
#         return max(0,rec(0,0,0))

# memoization
# class Solution:
#     def cherryPickup(self, grid):
#         n = len(grid) 
#         DP = [[[-1]*n for _ in range(n)] for _ in range(n)]
#         def rec(r1,c1,r2):
#             c2 = r1+c1 - r2
            
#             if not (0<=r1<n and 0<=r2<n and 0<=c1<n and 0<=c2<n and grid[r1][c1]!=-1 and grid[r2][c2]!=-1):
#                 return float('-inf')
#             if DP[r1][c1][r2]!=-1:
#                 return DP[r1][c1][r2]
#             if r1 == n-1 and c1== n-1:
#                 # it is understood that r2 == n-1 and c2 == n-1
#                 DP[r1][c1][r2] = grid[r1][c1]
#                 return DP[r1][c1][r2]
#             cur_cherry = 0
#             if r1==r2 and c1 == c2:
#                 cur_cherry = grid[r1][c1]
#             else:
#                 cur_cherry = grid[r1][c1]+grid[r2][c2]
#             best = max( rec(r1+1,c1,r2),rec(r1,c1+1,r2),rec(r1+1,c1,r2+1),rec(r1,c1+1,r2+1))
#             DP[r1][c1][r2] = best+cur_cherry
#             return DP[r1][c1][r2]
#         return max(0,rec(0,0,0))

#  Memoization: r2 = r1+c1 - c2
# class Solution:
#     def cherryPickup(self, grid):
#         n = len(grid) 
#         DP = [[[-1]*n for _ in range(n)] for _ in range(n)] 
#         def rec(r1,c1,c2):
#             r2 = r1+c1 - c2
#             if not (0<=r1<n and 0<=r2<n and 0<=c1<n and 0<=c2<n and grid[r1][c1]!=-1 and grid[r2][c2]!=-1):
#                 return float('-inf')
#             if DP[r1][c1][c2]!=-1:
#                 return DP[r1][c1][c2]
#             if r1 == n-1 and c1== n-1:
#                 # it is understood that r2 == n-1 and c2 == n-1
#                 DP[r1][c1][c2] = grid[r1][c1]
#                 return DP[r1][c1][c2]
#             cur_cherry = 0
#             if r1==r2 and c1 == c2:
#                 cur_cherry = grid[r1][c1]
#             else:
#                 cur_cherry = grid[r1][c1]+grid[r2][c2]
#             best = max( rec(r1+1,c1,c2),rec(r1,c1+1,c2),rec(r1+1,c1,c2+1),rec(r1,c1+1,c2+1))
#             DP[r1][c1][c2] = best+cur_cherry
#             return DP[r1][c1][c2]
#         return max(0,rec(0,0,0))

# Tabulation
# class Solution:
#     def cherryPickup(self, grid):
#         n = len(grid) 
#         DP = [[[float('-inf')]*n for _ in range(n)] for _ in range(n)] 
#         DP[0][0][0] = grid[0][0]
#         for c1 in range(1,n):
#             if grid[0][c1] == -1:
#                 break
#             # c1==c2
#             DP[0][c1][c1]= DP[0][c1-1][c1-1]+grid[0][c1]
#         for r1 in range(1,n):
#             if grid[r1][0] == -1:
#                 break
#             DP[r1][0][0] = DP[r1-1][0][0]+grid[r1][0]

#         for r1 in range(1,n):
#             for c1 in range(n):
#                 for c2 in range(n):
#                     r2 = r1+c1 - c2
#                     if not (0 <= r2 < n):
#                         continue
#                     if grid[r1][c1]==-1 or grid[r2][c2]==-1:
#                         # DP[r1][c1][c2] = 0
#                         continue
#                     cur_cherry = 0
#                     if r1==r2 and c1 == c2:
#                         cur_cherry = grid[r1][c1]
#                     else:
#                         cur_cherry = grid[r1][c1]+grid[r2][c2]
#                     best = max( DP[r1-1][c1][c2],DP[r1][c1-1][c2],DP[r1-1][c1][c2-1],DP[r1][c1-1][c2-1])
#                     DP[r1][c1][c2] = best+cur_cherry
#         return max(0,DP[n-1][n-1][n-1])

# Space reduction
class Solution:
    def cherryPickup(self, grid):
        n = len(grid) 
        DP = [[float('-inf')]*n for _ in range(n)]
        DP[0][0] = grid[0][0]
        for c1 in range(1,n):
            if grid[0][c1] == -1:
                break
            # c1==c2
            DP[c1][c1]= DP[c1-1][c1-1]+grid[0][c1]
        for r1 in range(1,n):
            newDP = [[float('-inf')] * n for _ in range(n)]
            for c1 in range(n):
                for c2 in range(n):
                    r2 = r1+c1 - c2
                    if not (0 <= r2 < n):
                        continue
                    if grid[r1][c1]==-1 or grid[r2][c2]==-1:
                        # DP[r1][c1][c2] = 0
                        continue
                    cur_cherry = 0
                    if r1==r2 and c1 == c2:
                        cur_cherry = grid[r1][c1]
                    else:
                        cur_cherry = grid[r1][c1]+grid[r2][c2]
                    # best = max( DP[c1][c2],DP[c1-1][c2],DP[c1][c2-1],DP[c1-1][c2-1])
                    best = max(
                        DP[c1][c2],
                        newDP[c1-1][c2] if c1 > 0 else float('-inf'),
                        DP[c1][c2-1] if c2 > 0 else float('-inf'),
                        newDP[c1-1][c2-1] if c1 > 0 and c2 > 0 else float('-inf')
                    )
                    newDP[c1][c2] = best+cur_cherry
            DP = newDP
        return max(0,DP[n-1][n-1])
