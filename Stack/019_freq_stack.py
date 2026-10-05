# https://leetcode.com/problems/maximum-frequency-stack/

import heapq
class FreqStack:

    def __init__(self):
        self.pq = []
        # track freq
        self.freq = defaultdict(int)
        # track order
        self.counter = 1

    def push(self, val: int) -> None:
        self.freq[val]+=1
        heapq.heappush(self.pq,(-1*self.freq[val],-1*(self.counter),val))
        self.counter+=1

    def pop(self) -> int:
        fq,order,value = heapq.heappop(self.pq)
        self.freq[value] -=1
        if self.freq[value] == 0:
            del self.freq[value]
        return value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
