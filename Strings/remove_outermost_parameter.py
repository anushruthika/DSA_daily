class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        s1=""
        for i in range(len(s)):
            if s[i] =="(":
                count+=1
                if count == 1:
                    continue 
            elif s[i] == ")":
                count-=1
                if count==0:
                    continue
            s1+=s[i]
        return s1
        
