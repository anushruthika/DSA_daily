#Count subarray with sum k
l=[2,3,-10,10,-5,5,5]
k=5
s=0
count=0
d={}
for i in range(len(l)):
    s+=l[i]
    if s == k:
        count+=1
    rem = s-k 
    if rem in d:
        count += d[rem]
    if s not in d:
        d[s]=1 
    else:
        d[s]+=1
print(count)

# XOR
l=[4,2,2,6,4]
k=6
s=0
count=0
d={}
for i in range(len(l)):
    s^=l[i]
    if s == k:
        count+=1
    rem = s^k 
    if rem in d:
        count += d[rem]
    if s not in d:
        d[s]=1 
    else:
        d[s]+=1
print(count)
