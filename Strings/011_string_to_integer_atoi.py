# Time Complexity: O(n)
# - strip() traverses the string once → O(n)
# - The while loop processes each character at most once → O(n)
# - int(ans) converts at most n digits to an integer → O(n)
# Overall: O(n)

# Space Complexity: O(n)
# - strip() creates a new string in Python → O(n)
# - ans stores up to all the digits of the input → O(n)
# Overall: O(n)

class Solution:
    def myAtoi(self, s: str) -> int:
        # O(n)- worst case to remove all leading zeros
        s=s.strip()
        if s == '':
            return 0
        n = len(s)
        sign = 1
        i=0
        if s[0] == '-':
            sign = -1
            i=1
        elif s[0] == '+':
            i=1
        ans=''
        while i<n:
            if s[i].isdigit():
                ans+=s[i]
            else:
                break
            i+=1
        print(ans)
        if ans=='':
            return 0
        x= sign*int(ans)
        if x > (2**31 - 1) :
            return (2**31-1)
        elif x < -(2**31):
            return -(2**31) 
        else:
            return x

        
