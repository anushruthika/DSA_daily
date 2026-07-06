# Time Complexity: O(n + k log k)
# Space Complexity: O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # st=''
        res = []
        for i in sorted(d.items(), key=lambda item: item[1],reverse=True) :
            # String concatination is costly costs O(n) every iteration
            # st+=i[0]*i[1]
            res.append(i[0]*i[1])
        return "".join(res)

# same approach using buitin Counter & one liner:
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([i[0]*i[1] for i in sorted(Counter(s).items(), key=lambda x: x[1],reverse=True)])

# Bucket Sort (mention only if asked for a better complexity)

# Time: O(n)
# Space: O(n)

# YET TO ADD
