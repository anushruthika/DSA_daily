# 973. K Closest Points to Origin

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []
        n = len(points)
        for i in range(n):
            dist = ((points[i][0])**2 + (points[i][1])**2 )**0.5
            heapq.heappush(pq,(-1*dist,points[i]))
            if len(pq)>k:
                heapq.heappop(pq)
        return [i[1] for i in pq]
