class Solution:
    def isValid(self, s: str) -> bool:
        d={']':'[','}':'{',')':'('}
        stack=[]
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif stack == [] and i in '}])':
                return False
            elif stack.pop(-1) !=d[i]:
                return False
        if stack:
            return False
        return True
