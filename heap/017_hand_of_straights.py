# 846. Hand of Straights

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize!=0:
            return False
        # O(n)
        d = Counter(hand)
        pq = list(d.items())
        heapq.heapify(pq)
        # O(n): O(n) becuase even if unqiue values exists the get added back according to frequency , m: number of unique values
        while pq:
            key,val = heapq.heappop(pq) 
            #  form straight
            temp = []
            # O(groupSize)
            for i in range(key+1,key+groupSize):
                if not pq:
                    return False
                cur,cur_val = heapq.heappop(pq)
                if cur!=i:
                    return False
                temp.append((cur,cur_val))
            # print(temp)
            if val>1:
                heapq.heappush(pq,(key,val-1))
            
            for i,j in temp:
                if j >1:
                    heapq.heappush(pq,(i,j-1))
        return True
        # for key in d:
        #     heapq.heappush(pq,(key,d[v]))
