# 295. Find Median from Data Stream
# addNum()    -> O(log n)
# findMedian()-> O(1)
# SC          -> O(n)
import heapq
class MedianFinder:

    def __init__(self):
        # stores first half=> max heap => small[0] stores middle element if odd & even
        self.small = []
        # stores second half=> min heap => large[0] stores middle element if even
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.small , -heappushpop(self.large,num))
        else:
            heapq.heappush(self.large , -heappushpop(self.small,-num))

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return -float(self.small[0])
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
