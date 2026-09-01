# https://www.geeksforgeeks.org/problems/steps-by-knight5927/1

# Time Complexity: O(n²)
# Space Complexity: O(n²)

from collections import deque
class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, n):
		directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
		queue = deque([(knightPos[0]-1,knightPos[1]-1,0)])
		seen = set()
		while queue:
		    r,c,steps = queue.popleft()
		    if r == targetPos[0]-1 and c == targetPos[1]-1:
		        return steps
		    for dr,dc in directions:
		        nr,nc = dr+r,dc+c
		        if 0<=nr<n and 0<=nc<n and (nr,nc) not in seen:
		            seen.add((nr,nc))
		            queue.append((nr,nc,steps+1))
		return -1
		
