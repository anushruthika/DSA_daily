# 901. Online Stock Span

# # TC: O(1) amortized per next()
# Amortized O(1) means even if one operation costs 100 and the remaining 99 cost 0, the average cost across 100 operations is still 1 per operation.
# SC: O(n)
# monotonic decreasing stack
class StockSpanner:
    def __init__(self):
        self.stack=[]
        self.d={}

    def next(self, price: int) -> int:
        result=1
        while self.stack and self.stack[-1]<=price:
            result+=self.d[self.stack.pop()]
        self.stack.append(price)
        self.d[price]=result
        return result
