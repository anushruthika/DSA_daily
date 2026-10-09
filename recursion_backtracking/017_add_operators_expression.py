# 282. Expression Add Operators

class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        def dfs(ind,exp,tot,prev):
            if ind == len(num):
                if tot == target:
                    res.append(exp)
                return
            # prev is recorded for multiplication
            for j in range(ind,len(num)):
                s = num[ind:j+1]
                if len(s)>1 and s[0]=="0":
                    continue
                x = int(s)
                if ind == 0:
                    dfs(j+1,s,x,x)
                else:
                    dfs(j+1,exp+'+'+s,tot+x,x)
                    dfs(j+1,exp+'-'+s,tot-x,-x)
                    dfs(j+1,exp+'*'+s,tot-prev+prev*x,prev*x)

        dfs(0,"",0,0)
        return res
