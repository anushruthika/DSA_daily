class Solution:
    def beautySum(self, s: str) -> int:
        count=0
        n=len(s)
        for i in range(n-2):
            d = Counter(s[i:i+3])
            for j in range(i+3,n):
                count+= max(d.values()) - min(d.values())
                d[s[j]]+=1
            count+= max(d.values()) - min(d.values())
        return count

#best solution
class Solution:
    def beautySum(self, s: str) -> int:
        count=0
        n=len(s)
        for i in range(n-2):
            d = defaultdict(int)
            for j in range(i,n):
                d[s[j]]+=1
                count+= max(d.values()) - min(d.values())
        return count


        
