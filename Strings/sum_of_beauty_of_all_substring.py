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
# edge case: 
# 1. s = "" output = 0
# 2. s = "a" output = 0
# 3. s = "ab" output = 0 beauty
# s = "aa" output= 2- no min =0
# Outer loop : O(n)
# Inner loop : O(n)
# max/min    : O(k)

# Total = O(n² × k)
#  k = 26 Total = O(n² × 26) = O(n²)
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


        
