
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        n = len(s)
        res = []
        cur = []
        def dfs(ind,cur):
            if ind == n:
                res.append(" ".join(cur))
            for j in range(ind,len(s)):
                if s[ind:j+1] in wordSet:
                    cur.append(s[ind:j+1])
                    dfs(j+1,cur)
                    cur.pop()
        dfs(0,cur)
        return res
                
