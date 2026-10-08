# 767. Reorganize String

class Solution:
    def reorganizeString(self, s: str) -> str:
        d= Counter(s)
        pq = []
        for key in d:
            heapq.heappush(pq,(-1*(d[key]),key))
        ans = ""
        while len(pq)>1:
            freq1,a = heapq.heappop(pq)
            freq2,b = heapq.heappop(pq)
            if ans and ans[-1] == a:
                ans+=b+a
            else:
                ans+=a+b
            if -1*freq1>1:
                heapq.heappush(pq,(-1*(-1*freq1-1),a))
            if -1*freq2>1:
                heapq.heappush(pq,(-1*(-1*freq2-1),b))
        if pq:
            if pq[0][0]<=-2:
                return ""
            ans+=pq[0][1]
        return ans

