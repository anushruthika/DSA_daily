# https://www.geeksforgeeks.org/problems/reverse-a-stack/1

# this problem is not divide and conquer(eg: merge sort divide into half but here decarese by one.)
# thus # decrease-and-conquer (or decrease by one).

# ascending order means stack.pop() should give elements in ascending order. 
# Meaning store in stack(thinking like an array): should be descneding order

# in general stack sorting we can use two stacks but here, we use 1 stack and the recursion stack to process
# Method	Time	Extra Space
# One stack + recursion	O(n²)	O(n)
# Two stacks (iterative)	O(n²)	O(n)
class Solution:
    def insert(self, stack,temp):
        if not stack or stack[-1]<=temp:
            stack.append(temp)
            return
        val =  stack.pop()
        self.insert(stack,temp)
        stack.append(val)
        return
            
    def sortStack(self, st):
        if st:
            temp = st.pop()
            self.sortStack(st)
            self.insert(st,temp)
        return st
