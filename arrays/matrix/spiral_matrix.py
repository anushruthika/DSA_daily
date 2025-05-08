class Solution(object):
    def spiralOrder(self, matrix):
        t,b,l,r=0,len(matrix)-1,0,len(matrix[0])
        res=[]
        t,b,l,r=0,len(matrix)-1,0,len(matrix[0])-1
        x=len(matrix)*len(matrix[0])
        res=[]
        while(len(res)<x):
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            if(len(res)>=x):
                break
            r-=1
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            if(len(res)>=x):
                break
            b-=1
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res
