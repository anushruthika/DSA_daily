# O(n)   # TC
# O(1)   # SC
arr = [2,6,3,9,6,2,0]

largest = float('-inf')
second = float('-inf')

for i in arr:
    if i > largest:
        second = largest
        largest = i

    elif largest > i > second:
        second = i

print(second)
