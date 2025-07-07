class MinStack(object):

    def __init__(self):
        self.min_stack=[]
        self.s=[]

    def push(self, val):
        self.s.insert(0,val)
        if self.min_stack:
            self.min_stack.insert(0,min(val,self.min_stack[0]))
        else:
            self.min_stack.insert(0,val)
    def pop(self):
        self.s.pop(0)
        self.min_stack.pop(0)
    def top(self):
        return self.s[0]
        

    def getMin(self):
        return self.min_stack[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack :
            self.min_stack.append(min(self.min_stack[-1],val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
