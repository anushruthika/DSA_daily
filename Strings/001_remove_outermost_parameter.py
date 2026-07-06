# 1021. Remove Outermost Parentheses

# considerations: 
# s is a valid parenthisis string, i.e.: s = ')(' not possible
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        stack = []
        for i in s:
            if i =='(':
                count+=1
                if count ==1:
                    continue
            else:
                count-=1
                if count ==0:
                    continue
            stack.append(i)
        return "".join(stack)
        
