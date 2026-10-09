# TC: O(nlogn)

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # Approach : sort based on starting time
        # reason: start adding passengers from the beggining time
        # maintain a minHeap to track the end time, Every time see how many trips end to track passengers get down(end time) before the current start time.
        trips.sort(key= lambda x:x[1])
        cur_pass = 0
        pq = []
        # O(n) n: trips 
        # inner while loop at max runs n times only(max n trips only n trips can be poped.)
        # O(nlogn)
        for trip in trips:
            # check trips got over according to current start time?
            while pq and pq[0][0]<=trip[1]:
                end_time,passen = heapq.heappop(pq)
                # trip got over so remove passen
                cur_pass-=passen
            # add cur trip pass
            cur_pass+=trip[0]
            if cur_pass>capacity:
                return False
            heapq.heappush(pq,(trip[2],trip[0]))
        return True

