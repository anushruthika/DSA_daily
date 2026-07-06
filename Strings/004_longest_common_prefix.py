# 14. Longest Common Prefix

# Time Complexity: O(n × m)
# Auxiliary Space: O(1)
# Space Complexity (including returned string): O(m)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        n = len(strs)
        res = len(strs[0])
        while i<n-1:
            s1,s2 = strs[i],strs[i+1]
            n1,n2 = len(s1),len(s2)
            count = 0
            j=0
            k=0
            while j<n1 and k<n2:
                if s1[j] == s2[k] :
                    count+=1
                else:
                    break
                j+=1
                k+=1
            res = min(count,res)
            i+=1
        return strs[0][:res]

 
