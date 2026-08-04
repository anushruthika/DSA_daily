# TC:  O(n*2**(2n)) = O(n*2**n) -> O(n): to generate new strings every time. can be ignored. but O(2**2*n) is to recurse and create list
# SC: O(2**2*n)
class Solution:
    def __init__(self):
        self.res = []
    def take_leave(self,open,close,op,n):
        if len(op)>=2*n:
            self.res.append(op)
            return
        if open<n:
            self.take_leave(open+1,close,op+"(",n)
        if open>close:
            self.take_leave(open,close+1,op+")",n)
    def generateParenthesis(self, n: int) -> List[str]:
        self.take_leave(0,0,"",n)
        return self.res
