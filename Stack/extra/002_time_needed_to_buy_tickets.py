# 2073. Time Needed to Buy Tickets

from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        queue = deque()
        for ind,val in enumerate(tickets):
            queue.append((val,ind))
        while queue:
            x,index = queue.popleft()
            if index == k and x-1==0:
                return count+1
            if x-1>0:
                queue.append((x-1,index))
            count+=1
