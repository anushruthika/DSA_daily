# https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1

class Solution:
    def __init__(self):
        self.res = []
    def construct(self,op,n):
        if len(op)>=n:
            self.res.append(op)
            return
        # if not op or op[-1] == "0":
        self.construct(op+"0",n)
        self.construct(op+"1",n)
    def binstr(self, n):
        self.construct("",n)
        return self.res
        
