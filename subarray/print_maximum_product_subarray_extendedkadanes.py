import math
l=list(map(int,input().split(",")))
# l=[2,3,-8,7,-1,2,3]
# l=[-2, -5, 6, -2, -3, 1, 5, -6]
s=0
m=-math.inf 
n=len(l)
# j and k two pointers. j is updated whenever the sum becomes 0 and k is updated 
j=m_j=m_k=0
for i in range(0,n):
    s+=l[i]
    if s<0:
       s=0
       j=i+1
    if m<s:
        m=s 
        m_j=j 
        m_k=i+1 

print(l[m_j:m_k])
