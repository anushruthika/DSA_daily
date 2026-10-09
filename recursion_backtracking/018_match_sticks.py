# 473. Matchsticks to Square

class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        tot = sum(matchsticks)
        if tot%4!=0:
            return False
        side = tot/4
        matchsticks.sort(reverse= True)
        count = [0,0,0,0]
        n = len(matchsticks)
        def dfs(i,count):
            if i == n:
                if count[0] == count[1] == count[2] == count[3]:
                    return True
            for ind in range(4):
                if matchsticks[i]+count[ind]<=side:
                    count[ind]+=matchsticks[i]
                    if dfs(i+1,count):
                        return True
                    count[ind]-=matchsticks[i]
            return False
        return dfs(0,count)
