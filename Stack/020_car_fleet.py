# 853. Car Fleet

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        stack=[]
        n = len(position)
        for pos,sp in cars:
            time = (target-pos)/sp
            stack.append(time)
            while len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
