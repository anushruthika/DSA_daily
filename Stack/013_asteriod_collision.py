# 735. Asteroid Collision
# TC: O(n) SC: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                # current asteroid destroys stack top
                if stack[-1] < abs(i):
                    stack.pop()
                    continue
                # case : ateroids = [8,-8] output=[]
                # both destroy each other
                elif stack[-1] == abs(i):
                    stack.pop()
                # current asteroid destroyed
                break
            else:
                stack.append(i)
        return stack
