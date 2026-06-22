
# EDGE CASE
# | Job ID | Deadline | Profit |
# | ------ | -------- | ------ |
# | 1      | 4        | 20     |
# | 2      | 5        | 60     |
# | 3      | 6        | 70     |
# | 4      | 6        | 65     |
# | 5      | 4        | 25     |
# | 6      | 2        | 80     |
# | 7      | 2        | 10     |
# | 8      | 2        | 22     |


############################ BRUTE FORCE




############################ GREEDY NAIVE APPROACH
# TC: O(n log n + n * max_deadline)
# SC: # SC: O(max_deadline)

import heapq
class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = []
        for i in range(len(profit)):
            jobs.append((profit[i],deadline[i]))
        jobs.sort(reverse= True)
        count =0
        tot = 0
        arr = [False]*max(deadline)
        for p,d in jobs:
            # print(p,d,arr,count,tot)
            while d-1>=0:
                if not arr[d-1]:
                    arr[d-1] = p
                    count+=1
                    tot+=p
                    break
                d -=1
        return [count,tot]
                    
            
                
