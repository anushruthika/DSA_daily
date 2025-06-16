class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s2.insert(0,x)
        while self.s1:
            self.s2.insert(0,(self.s1.pop(-1)))
        self.s1,self.s2=self.s2,self.s1
    def pop(self) -> int:
        return self.s1.pop(0)

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return not(len(self.s1))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
