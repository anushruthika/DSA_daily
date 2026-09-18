
# TC: O((kT)^n)
s = ['t','t','p','p','t','p']
m = len(s)
k = 2
p = [2,3,5]
n = len(p)
t = [0,1,4]
# def rec(ind,theives):
#     if ind == n:
#         return 0
#     maximize = 0
#     for thf in range(max(0,-k+p[ind]),max(k+p[ind],m)):
#         if thf in theives:
#             i = theives.index(thf)
#             maximize = max(maximize,1+rec(ind+1,theives[:i]+theives[i+1:]))
#     return maximize
# print(rec(0,t))

# memoization : 2^T *KT * n

from collections import deque
p = deque([])
t = deque([])
count = 0
for i in range(m):
    if s[i] == 'p':
        p.append(i)
    else:
        t.append(i)
    while p and t:
        pol = p[0]
        thf = t[0]
        if abs(pol-thf)<=k:
            count+=1
            p.popleft()
            t.popleft()
        elif pol<thf:
            p.popleft()
        elif thf<pol:
            t.popleft()
print(count)
        
            
            
    
    
    
