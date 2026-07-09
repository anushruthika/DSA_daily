# https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1

# Time Complexity: O(n)
# Space Complexity: O(k) (or O(Σ) where Σ is the character set size)

class Solution:
    def atmost(self,s,k):
        freq = {}
        left = 0
        res = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            while len(freq)>k:
                freq[s[left]]-=1
              # Needed to remove if s[left] becomes zero orelse the instance exists even if it becomes.
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left+=1
            res+=right-left+1
        return res
            
    def countSubstr (self, s, k):
        if k == 0:
            return 0
        return self.atmost(s,k) - self.atmost(s,k-1)
