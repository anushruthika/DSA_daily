# youtube interview with nithish (keerthi)
import heapq
arr = [2,4,8,2]
k = 4

# [2,2,4,8]
# 1st : [2,2,4,8//2] => [2,2,4,4,4]
# 2nd : [2,2,4,4,2,2]
# 3rd: [2,2,4,2,2,2,2]
# 4th: [2,2,2,2,2,2,2,2]
pq = []
for i in arr:
    pq.append(-i)
i = 0
while i<k:
    x = heapq.heappop(pq)
    val = -1*x 
    if val%2 == 0:
        heapq.heappush(pq,-1*(val//2))
        heapq.heappush(pq,-1* (val//2))
    else:
        heapq.heappush(pq,-1*(val//2+1))
        heapq.heappush(pq,-1*(val//2))
# returns the maximum elemnt in the arr after splitting
return -1*heaq.heappop(pq)
    
    
