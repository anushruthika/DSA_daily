# 131. Palindrome Partitioning

# Time: O(n · 2ⁿ) 2ⁿ recursion and O(n) for palindrome 
# Space: O(2^n+n) = O(2^n) for storing res& path

# worst case eg: s = "aaaa"
# ["a","a","a","a"]
# ["a","a","aa"]
# ["a","aa","a"]
# ["a","aaa"]
# ["aa","a","a"]
# ["aa","aa"]
# ["aaa","a"]
# ["aaaa"]
#  n = 4 and the partitions is 8 meaning 2^(n-1) sc & tc

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def rec(index,path):
            if index == n:
                res.append(path.copy())
            for i in range(index+1,n+1):
                if s[index:i] == s[index:i][::-1]:
                    path.append(s[index:i])
                    rec(i,path)
                    path.pop()
        rec(0,[])
        return res
