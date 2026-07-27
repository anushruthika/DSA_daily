# https://www.geeksforgeeks.org/problems/reverse-a-stack/1

# time complexity O(n**2)
# space complexity : O(n) recursion stack
class Solution:
    
    def rev(self,stack,temp):
        if not stack:
            stack.append(temp)
            return
        val = stack.pop()
        self.rev(stack,temp)
        stack.append(val)
    def reverseStack(self, st):
        if st:
            temp = st.pop()
            self.reverseStack(st)
            self.rev(st,temp)
        return st
