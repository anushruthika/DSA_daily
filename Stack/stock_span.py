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
