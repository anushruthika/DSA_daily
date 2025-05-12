class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        i=0
        if s=='':
            return 0
        if s[0] == '-':
            sign=-1
            i=1
        elif s[0] =='+':
            i=1
        st=''
        
        while i <len(s) and ord(s[i])>=48 and ord(s[i])<=57:
            if s[i].isalpha() and i!=0:
                print(s)
                break
            st+=s[i]
            print(st)
            i+=1
            
        if st=='':
            return 0
        # return sign* int(st)
        x= sign*int(st)
        if x > (2**31 - 1) :
            return (2**31-1)
        elif x < -(2**31):
            return -(2**31) 
        else:
            return x
        
