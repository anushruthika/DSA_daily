# 1834. Single-Threaded CPU

import heapq
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        queue = deque(sorted([(t[0],t[1],i) for i,t in enumerate(tasks)],key = lambda x:x[0])) #enqueue time, processing time, index
        pq = [] # available tasks
        pt = 1
        ans = []
        while queue or pq:
            while queue and queue[0][0]<=pt:
                ent,prt,ind = queue.popleft()
                heapq.heappush(pq,(prt,ind))
            if pq:
                prt,ind = heapq.heappop(pq)
                ans.append(ind)
                pt+=prt
            # idle cpu
            else:
                # causes TLE
                # pt+=1
                # jump directly to next task enqtime
                pt=queue[0][0]
        return ans
