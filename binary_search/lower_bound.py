
arr= [1,2,2,3]
target=2
arr= [3,5,8,15,19] 
target = 9
low = 0
high = len(arr) - 1
flag=1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        flag=0
        print(mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if flag==1:
    print(low)
