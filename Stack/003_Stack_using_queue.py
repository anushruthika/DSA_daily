# 225. Implement Stack using Queues
# __init__
# TC: O(1)
# SC: O(1)

# push
# TC: O(n)
# SC: O(n)

# pop
# TC: O(1)
# SC: O(1)

# top
# TC: O(1)
# SC: O(1)

# empty
# TC: O(1)
# SC: O(1)
from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]        

    def empty(self) -> bool:
        return not(len(self.q1))


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
