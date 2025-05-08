3 variations
# print nth row
n = int(input())
# if n==1:
#     return [1]
# if n==2:
#     return [1,1]
#instance of previous row
a=[1,1]
for i in range(3,n+1):
    #next row
    arr=[1]
    for j in range(1,i-1):
        arr.append(a[j-1]+a[j])
    arr.append(1)
    a=arr
print(arr)

#print(whole array until row)
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        if n==2:
            return [[1],[1,1]]
        #instance of previous row
        a=[[1],[1,1]]
        for i in range(3,n+1):
            #next row
            arr=[1]
            for j in range(1,i-1):
                arr.append(a[i-2][j-1]+a[i-2][j])
            arr.append(1)
            a.append(arr)
        return a
# print value present in rth row and cth column
r,c = int(input()),int(input())
# if n==1:
#     return [[1]]
# if n==2:
#     return [[1],[1,1]]
#instance of previous row
a=[[1],[1,1]]
for i in range(3,r+1):
    #next row
    arr=[1]
    for j in range(1,i-1):
        arr.append(a[i-2][j-1]+a[i-2][j])
    arr.append(1)
    a.append(arr)
print(arr[c-1])
        

