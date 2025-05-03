# Longest sub array with sum k (negatives and positive number both)
l=[2,3,5]
k=5
s=0
count=0
d={}
for i in range(len(l)):
    s+=l[i]
    if s == k:
        count = max(count,i+1)
    rem = s-k 
    if rem in d:
        count = max(count,(i+1)-d[rem])
    if s not in d:
        d[s]=i+1
print(count)

