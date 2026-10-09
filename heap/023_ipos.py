# 502. IPO

class Solution:
    # we wont subtract the capital
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        if k == 0:
            return w
        # for to pick an ipo, i should pick from ipos that base capital <=w
        # w: represents profits
        # cur_cap represents capacit
        cur_cap = w
        # sort array based on capital 
        n = len(profits)
        ipos = list(zip(capital,profits))

        # no need to sort based on max profit(becuase heap will do it for us)
        ipos.sort(key = lambda x:x[0])
        ipos = deque(ipos)
        # initial heap
        pq = []
        while len(ipos)>0 and ipos[0][0]<=w:
            heapq.heappush(pq,-1*(ipos[-0][1]))
            ipos.popleft()
           
        while pq and k>0:
            pro = heapq.heappop(pq)
            w+=-1*pro
            while len(ipos)>0 and ipos[0][0]<=w:
                heapq.heappush(pq,-1*(ipos[0][1]))
                ipos.popleft()
            k-=1
        return w
