# online gdb
# TC: O(n) SC: O(n)
pq = [-x for x in arr]
# o(n)=> heapify
heapq.heapify(pq)

# TC:O(nlogn) SC: o(n)
import heapq
def convert_min_to_max_heap(arr):
    pq =[]
    for i in arr:
        heapq.heappush(pq,-1*i)
    for i in range(len(pq)):
        pq[i] = pq[i]*-1
    return pq
