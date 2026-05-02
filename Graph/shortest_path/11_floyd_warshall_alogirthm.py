# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

# Time: O(V^3)
# Three nested loops (k, i, j), each runs V times
# For every pair (i, j), we try all possible intermediate nodes k
# So total operations = V * V * V = O(V^3)

# Space: O(V^2)
# We store distances in a V x V matrix (dist)
# No extra space used apart from this matrix
class Solution:
	def floydWarshall(self, dist):
        V = len(dist)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if dist[i][k]!=10**8 and dist[k][j]!=10**8 and dist[i][j]>dist[i][k]+dist[k][j]:
                        dist[i][j] = dist[i][k]+dist[k][j]
        return dist
