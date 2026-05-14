# https://www.geeksforgeeks.org/problems/steps-by-knight5927/1

# Time Complexity: O(n²)
# Space Complexity: O(n²)

from collections import deque
class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        # Convert to 0-based indexing
        sr, sc = knightPos[0] - 1, knightPos[1] - 1
        tr, tc = targetPos[0] - 1, targetPos[1] - 1
        # Knight moves
        directions = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]
        q = deque()
        q.append((sr, sc, 0))
        visited = set()
        visited.add((sr, sc))
        while q:
            r, c, steps = q.popleft()
            # Reached target
            if (r, c) == (tr, tc):
                return steps
            # Explore all knight moves
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # Valid cell
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc, steps + 1))

        return -1
