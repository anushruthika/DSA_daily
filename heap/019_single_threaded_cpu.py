# 1834. Single-Threaded CPU

from collections import deque
import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        n = len(tasks)

        queue = sorted((enqueue, i) for i, (enqueue, process) in enumerate(tasks))
        
        pq = []
        res = []
        time = 0
        i = 0

        while i < n or pq:

            # If no task is available, jump time to next task
            if not pq and time < queue[i][0]:
                time = queue[i][0]

            # Add all available tasks
            while i < n and queue[i][0] <= time:
                enqueue, ind = queue[i]
                heapq.heappush(pq, (tasks[ind][1], ind))
                i += 1

            # Process shortest processing time, then smallest index
            processing_time, ind = heapq.heappop(pq)
            res.append(ind)
            time += processing_time

        return res
