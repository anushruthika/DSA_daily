class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids:
            while stack and i<0<stack[0]:
                if abs(i)>abs(stack[0]):
                    stack.pop(0)
                elif abs(i)==abs(stack[0]):
                    stack.pop(0)
                    break
                else:
                    break
            else:
                stack.insert(0,i)
        # stack2=[]
        # while stack:
        #     stack2.insert(0,stack.pop(0))
        return stack[::-1]
