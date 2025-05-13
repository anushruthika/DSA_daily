s='landscape'
n=len(s)
print((n*(n+1))/2)

#one liner
print((n:=len(input())*(n+1))/2)

count=0
for i in range(n):
    for j in range(i+1,n+1):
        print(s[i:j])
        count+=1
print(count)
