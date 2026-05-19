# 844. Backspace String Compare

#Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def correct(self,s):
        
        i=len(s)-1
        new_s = ''
        skip=0
        while i>=0:
            if s[i] == '#':
                skip+=1
            elif skip>0:
                skip-=1
            else:
                new_s+=s[i]
            i-=1
        return new_s[::-1]
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.correct(s) == self.correct(t)
        
