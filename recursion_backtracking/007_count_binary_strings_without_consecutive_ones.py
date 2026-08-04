#  TC: O(n*2**n) O(n) for generating new string every time
# sc:auxillary : O(n) recursion stack
# additional space if needed: O(n**2) every time new string created.
class Solution:
    def __init__(self):
        # self.res = []
        self.count = 0
    def construct(self,op,n):
        if len(op)>=n:
            # self.res.append(op)
            self.count+=1
            return
        if not op or op[-1] == "0":
            self.construct(op+"1",n)
        self.construct(op+"0",n)
    def countStrings(self, n):
        self.construct("",n)
        # return len(self.res)
        return self.count
       
