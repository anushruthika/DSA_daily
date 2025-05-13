class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        st=''
        for i in sorted(d.items(), key=lambda item: item[1],reverse=True) :
            st+=i[0]*i[1]
        return st
