# 8. String to Integer (atoi)

# Time Complexity: O(n)
# space Complexity: 
# Recursion stack: O(n)
# String ans: O(n)
# You're building a new string recursively with: s[i] + func(i+1)

class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if s == '':
            return 0
        n = len(s)
        sign = 1
        def func(i):
            if not 0<=i<n:
                return ''
            if i==0 and ( s[0] == '-' or s[0] == '+'):
                nonlocal sign
                if s[0] == '-':
                    sign = -1
                    return func(i+1)
                elif s[0] == '+':
                    return func(i+1)
            elif s[i].isdigit():
                return s[i]+func(i+1)
            else:
                return ''
        ans = func(0)
        if ans=='':
            return 0
        x= sign*int(ans)
        if x > (2**31 - 1) :
            return (2**31-1)
        elif x < -(2**31):
            return -(2**31) 
        else:
            return x
